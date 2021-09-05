# @s = player that just placed a furnace
# run from advancement place_blast_furnace

advancement revoke @s only gm4_soul_glass:place_blast_furnace
summon area_effect_cloud ~ ~ ~ {Tags:["gm4_furnace_ray"]}
execute anchored eyes positioned ^ ^ ^ anchored feet run tp @e[tag=gm4_furnace_ray] ^ ^ ^ ~ ~
scoreboard players set gm4_ray_counter gm4_count 0
execute as @e[tag=gm4_furnace_ray] at @s run function gm4_soul_glass:furnace/ray
execute at @e[tag=gm4_furnace_ray] align xyz positioned ~0.5 ~0.5 ~0.5 unless entity @e[type=marker,distance=..0.1,tag=gm4_sg_furnace,limit=1] run summon marker ~ ~ ~ {CustomName:'"gm4_sg_furnace"',Tags:["gm4_sg_furnace"]}
kill @e[tag=gm4_furnace_ray]
