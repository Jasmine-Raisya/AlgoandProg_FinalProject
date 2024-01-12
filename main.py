import subprocess


class MobileLegendsRoleGenerator:
  ROLES = {
      "Marksman": ["Backline", "Highground"],
      "Tank": ["Rusher", "Frontline"],
      "Mage": ["Highground", "Backline"],
      "Assassin": ["Rusher", "Backline"],
      "Support": ["Frontline", "Backline"]
  }

  def __init__(self):
    self.user_preferences = {}

  def set_preference(self, key, value):
    self.user_preferences[key] = value

  def get_preference(self, key):
    return self.user_preferences.get(key)

  def generate_suitable_role(self):
    rotation_preference = self.get_preference("rotation")
    scaling_preference = self.get_preference("scaling")

    if rotation_preference == "Turret-Focused" and scaling_preference == "Item":
      return "Marksman"
    elif rotation_preference == "Turret-Focused" and scaling_preference == "Skill":
      return "Marksman"
    elif rotation_preference == "Jungle-Focused" and scaling_preference == "Item":
      return "Assassin"
    elif rotation_preference == "Jungle-Focused" and scaling_preference == "Skill":
      return "Assassin"
    elif rotation_preference == "Enemy-Mirroring" and scaling_preference == "Item":
      return "Mage"
    elif rotation_preference == "Enemy-Mirroring" and scaling_preference == "Skill":
      return "Support"
    elif rotation_preference == "Cover" and scaling_preference == "Item":
      return "Support"
    elif rotation_preference == "Cover" and scaling_preference == "Skill":
      return "Tank"
    else:
      return "Role not determined based on preferences."

  def ask_positioning_preference(self):
    role = self.generate_suitable_role()
    if role in MobileLegendsRoleGenerator.ROLES:
      print(f"Positioning Preferences for {role}:")
      print(", ".join(MobileLegendsRoleGenerator.ROLES[role]))
      positioning_preference = input(
          f"Enter your preferred positioning ({', '.join(MobileLegendsRoleGenerator.ROLES[role])}): "
      )
      self.set_preference("positioning", positioning_preference.capitalize())
    else:
      print(
          f"Positioning preferences are not applicable for the determined role: {role}"
      )

  def run_file(self):
    role = self.generate_suitable_role()
    files = {
        "Marksman": "Marksman.py",
        "Mage": "Mage.py",
        "Assassin": "Assassin.py",
        "Support": "Support.py",
        "Tank": "Tank.py"
    }
    if role in files:
      file = files[role]
      subprocess.run(["python", file])
      subprocess.call(["python", file])
    else:
      print("Invalid role")


def main():
  ml_role_generator = MobileLegendsRoleGenerator()

  rotation_preference = input(
      "Enter your preferred rotation style (Turret-Focused, Jungle-Focused, Enemy-Mirroring, Cover): "
  )
  scaling_preference = input(
      "Enter your preferred scaling prioritization (Skill, Item): ")

  ml_role_generator.set_preference("rotation", rotation_preference)
  ml_role_generator.set_preference("scaling", scaling_preference)

  ml_role_generator.ask_positioning_preference()
  print(
      f"Based on your preferences, the suitable role is: {ml_role_generator.generate_suitable_role()}"
  )

  ml_role_generator.run_file()


if __name__ == "__main__":
  main()
