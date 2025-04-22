#!/bin/bash

echo "🔍 Vérification des vulnérabilités NuGet..."

# On liste les vulnérabilités
vuln_output=$(dotnet list package --vulnerable --include-transitive)

# On affiche le résultat
echo "$vuln_output"

# On check s'il y a une ligne qui parle de vulnérabilités
if echo "$vuln_output" | grep -q "High"; then
  echo "❌ Des vulnérabilités ont été détectées !"
  exit 1
else
  echo "✅ Aucun package vulnérable détecté."
fi
