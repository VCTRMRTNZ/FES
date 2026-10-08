## ⚡ Git + GitHub — Chuleta rápida

### 🆕 Crear programa / rama nueva

```powershell
git switch main
git pull
git switch -c nombre-rama

# TRABAJAR

git add .
git commit -m "Descripción"
git push -u origin nombre-rama
```

### 🔧 Continuar programa existente

```powershell
git switch nombre-rama
git pull

# TRABAJAR

git add .
git commit -m "Descripción"
git push
```

### 🌿 Ramas

```powershell
git branch              # Ver ramas locales
git branch -a           # Ver todas
git switch nombre-rama  # Cambiar
git switch -c nombre    # Crear + cambiar
```

### 🔄 Cambios

```powershell
git status   # Ver cambios
git add .    # Preparar
git commit -m "..."  # Guardar
git push     # Subir
git pull     # Descargar
```

### 📜 Historial

```powershell
git log --oneline
```

### ⚠️ `src refspec main does not match any`

```powershell
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

### 🧠 Flujo mental

**TRABAJAR → `status` → `add` → `commit` → `push`**
