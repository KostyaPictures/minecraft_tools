mode=1
#mode2="xz" #xy
#1 - just commands from input_commands.txt
#2 - advanced mode with building of redstone circuit with command blocks (WIP)

if mode==1:
    with open("input_commands.txt") as f:
        commands=f.read().replace("\\","\\\\").replace("\"","\\\"").split("\n")

    if len(commands)<2:
        print("WARNING! Do not use this generator with less than two commands")

    start=f"summon minecraft:command_block_minecart ~ ~ ~-1 {{Command:\"{commands[0]}\", Passengers:["
    end="{id:\"minecraft:command_block_minecart\",Command:\"kill @e[type=minecraft:command_block_minecart,distance=..1]\"}]}"
    result=""
    result+=start
    for command in commands[1:]:
        middle=f"{{id:\"minecraft:command_block_minecart\", Command:\"{command}\"}},"
        result+=middle
    result+=end

    print(result)