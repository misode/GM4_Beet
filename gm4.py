from beet.toolchain.helpers import subproject
from beet import Context
import json
import os
import subprocess

BASE = "base"
OUTPUT = "out"
RELEASE = "release"


def run(cmd: list[str]) -> str:
	return subprocess.run(cmd, capture_output=True, encoding="utf8").stdout.strip()


def build_modules(ctx: Context):
	with open("meta.json", "r") as f:
		version_meta = json.load(f)
		prefix = version_meta["patch_prefix"]
		version = version_meta["version"]

	modules = [{"id": p.name} for p in sorted(ctx.directory.glob("gm4_*"))]
	print(f"[GM4] Found {len(modules)} modules")

	head = run(["git", "rev-parse", "HEAD"])
	try:
		with open(f"{RELEASE}/{version}/meta.json", "r") as f:
			meta = json.load(f)
			released_modules = meta["modules"]
			last_commit = meta["last_commit"]
	except:
		released_modules = []
		last_commit = None

	print(f"version={version} HEAD={head} last={last_commit}")
	for module in modules:
		id = module["id"]
		if last_commit:
			module["diff"] = run(["git", "diff", f"{last_commit}..HEAD", "--shortstat", "--", BASE, id])
		else:
			module["diff"] = True

		released: dict | None = next((m for m in released_modules if m["id"] == id), None)
		if not module["diff"] and released:
			module.update(released)
			print(f"Keeping {id}, no changes")
			continue

		module["patch"] = released["patch"] + 1 if released else prefix

		try:
			with open(f"{id}/pack.mcmeta", "r") as f:
				meta: dict = json.load(f)
				module["name"] = meta.get("module_name", id)
				module["description"] = meta.get("site_description", "")
				module["categories"] = meta.get("site_categories", [])
				module["hidden"] = meta.get("hidden", False)
				print(f"Updating {id}: {module['patch']}")
		except:
			module["id"] = None

	module_updates = [{k: m[k] for k in ["id", "name", "patch"]} for m in modules if m["id"]]

	for module in modules:
		id = module["id"]
		if not id:
			continue
		ctx.require(subproject({
			"id": id,
			"data_pack": {
				"name": id,
				"load": [BASE, id],
				"zipped": True,
			},
			"output": OUTPUT,
			"pipeline": [
				"gm4.module_updates"
			],
			"meta": {
				"id": id,
				"module_updates": module_updates
			}
		}))
		print(f"Generated {id}")

	os.makedirs(OUTPUT, exist_ok=True)
	with open(f"{OUTPUT}/meta.json", "w") as f:
		out = {
			"last_commit": head,
			"modules": [m for m in modules if m.get("id") is not None],
		}
		json.dump(out, f, indent=2)
		f.write('\n')


def module_updates(ctx: Context):
	init = ctx.data.functions[f"{ctx.meta['id']}:init"]
	init.lines.remove("#$moduleUpdateList")
	init.lines.append('# Module update list')
	init.lines.append('data remove storage gm4:log queue[{type:"outdated"}]')
	for m in ctx.meta["module_updates"]:
		init.lines.append(f'execute if score {m["id"]} gm4_modules matches ..18000 run data modify storage gm4:log queue append value {{type:"outdated",module:"{m["name"]}"}}')
