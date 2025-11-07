characters = []

for i in range(3):
    name = input("🔼 ").strip()
    attack = int(input("🔼 "))
    defense = int(input("🔼 "))
    characters.append([name, (attack, defense)])

print("🔽", characters)

max_attack = characters[0][1][0]
max_attack_name = characters[0][0]
max_defense = characters[0][1][1]
max_defense_name = characters[0][0]

for name, (attack, defense) in characters[1:]:
    if attack > max_attack:
        max_attack = attack
        max_attack_name = name
    if defense > max_defense:
        max_defense = defense
        max_defense_name = name

print(f"🔽 attack {max_attack_name} {max_attack}")
print(f"🔽 defense {max_defense_name} {max_defense}")
