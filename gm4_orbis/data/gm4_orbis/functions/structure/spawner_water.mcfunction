# spawn a random spawner type based on the bedrock pattern
setblock ~ ~ ~ air
execute unless block ~ -61 ~ bedrock unless block ~ -60 ~ bedrock run setblock ~ ~ ~ spawner{SpawnPotentials:[{weight:1,data:{entity:{id:"drowned",DeathLootTable:"gm4_orbis:entities/drowned"}}}]}
execute unless block ~ -61 ~ bedrock if block ~ -60 ~ bedrock run setblock ~ ~ ~ spawner{SpawnPotentials:[{weight:1,data:{entity:{id:"guardian",DeathLootTable:"gm4_orbis:entities/guardian"}}}]}
execute if block ~ -61 ~ bedrock unless block ~ -60 ~ bedrock run setblock ~ ~ ~ spawner{SpawnPotentials:[{weight:1,data:{entity:{id:"guardian",DeathLootTable:"gm4_orbis:entities/guardian"}}}]}
execute if block ~ -61 ~ bedrock if block ~ -60 ~ bedrock run setblock ~ ~ ~ spawner{SpawnPotentials:[{weight:1,data:{entity:{id:"pufferfish",DeathLootTable:"gm4_orbis:entities/pufferfish"}}}]}
