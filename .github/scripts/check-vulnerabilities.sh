#!/bin/bash

echo "🔍 Vérification des vulnérabilités NuGet..."

# On liste les vulnérabilités
vuln_output=$(dotnet list package --vulnerable)

# On affiche le résultat
echo "$vuln_output"

# On check s'il y a une ligne qui parle de vulnérabilités
if echo "$vuln_output" | grep -q "has the following vulnerable packages"; then
  echo "❌ Des vulnérabilités ont été détectées !"
  exit 1
else
  echo "✅ Aucun package vulnérable détecté."
fi
