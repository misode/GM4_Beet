# @s = player holding an Audere tool
# at @s
# run from active_tool

scoreboard players operation $tool_max_damage gm4_ml_data -= $tool_current_damage gm4_ml_data

execute if score $tool_max_damage gm4_ml_data matches 424..1148 run effect give @s minecraft:haste 2 0
execute if score $tool_max_damage gm4_ml_data matches 156..423 run effect give @s minecraft:haste 2 1
execute if score $tool_max_damage gm4_ml_data matches 59..155 run effect give @s minecraft:haste 2 2
execute if score $tool_max_damage gm4_ml_data matches ..57 run effect give @s minecraft:haste 2 3
