#!/bin/bash

commit_message="$1"

echo "📋 Commit message reçu : $commit_message"

if [[ "$commit_message" != *🚀* ]]; then
  echo "❌ Le message de commit doit contenir une fusée 🚀"
  exit 1
else
  echo "✅ Emoji fusée détecté !"
fi
