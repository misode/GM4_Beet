# @s = armor_stand being moved
# at @s
# run from move/moving

# round to nearest 15 degrees of a block
execute store result score $as_rot_y gm4_bas_data run data get entity @s Rotation[0] .06667
execute store result entity @s Rotation[0] float 15 run scoreboard players get $as_rot_y gm4_bas_data
