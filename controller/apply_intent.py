import yaml
import subprocess

with open("intent/intent.yaml") as f:
    intent = yaml.safe_load(f)

allowed_ports = intent["security"]["allowed_ports"]

subprocess.run(["ufw", "--force", "reset"])
subprocess.run(["ufw", "default", "deny", "incoming"])
subprocess.run(["ufw", "default", "allow", "outgoing"])

for port in allowed_ports:
    subprocess.run(["ufw", "allow", f"{port}/tcp"])

subprocess.run(["ufw", "--force", "enable"])

print("Réseau conforme à l’intention Git")