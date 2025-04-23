import subprocess
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')
print("🔍 Vérification des dépendances circulaires dans les packages NuGet...")

try:
    result = subprocess.run(
        ["dotnet", "list", "package", "--include-transitive"],
        capture_output=True,
        text=True,
        check=True
    )
except subprocess.CalledProcessError as e:
    print("❌ Erreur lors de l'exécution de dotnet list package")
    print(e.stdout)
    sys.exit(1)

lines = result.stdout.splitlines()
graph = defaultdict(list)
current_package = None

for line in lines:
    if ">" in line:
        parts = line.strip().split(">")
        if len(parts) == 2:
            parent = parts[0].strip()
            child = parts[1].strip().split(" ")[0]  # enlever version
            graph[parent].append(child)

# Détection de cycle
def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(v):
        visited.add(v)
        rec_stack.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(v)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

if has_cycle(graph):
    print("❌ Cycle détecté dans les dépendances NuGet !")
    sys.exit(1)
else:
    print("✅ Aucun cycle de dépendance NuGet détecté.")
