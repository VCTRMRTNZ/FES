# Git & GitHub — Cheat Sheet

Guía rápida para trabajar con **Git + GitHub desde VS Code en Windows 11**.

---

## 📌 Flujo básico

Los comandos que más utilizarás:

```powershell
git status
git add .
git commit -m "Descripción de los cambios"
git push
```

Flujo:

```text
TRABAJAR EN EL CÓDIGO
        ↓
   git status
        ↓
    git add .
        ↓
git commit -m "..."
        ↓
     git push
```

---

# 🌿 1. Crear una nueva rama

Utiliza este escenario cuando quieras empezar un **programa o funcionalidad nueva** sin modificar directamente `main`.

### 1. Ir a `main`

```powershell
git switch main
```

### 2. Actualizar `main`

```powershell
git pull
```

### 3. Crear la nueva rama y cambiarte a ella

```powershell
git switch -c nombre-nueva-rama
```

A partir de este momento estás trabajando en:

```text
nueva-rama
```

### 4. Trabajar en el código

Crea/modifica tus archivos normalmente desde VS Code.

### 5. Comprobar los cambios

```powershell
git status
```

### 6. Preparar los cambios

```powershell
git add .
```

### 7. Crear un commit

```powershell
git commit -m "LO QUE SEA"
```

### 8. Subir la rama a GitHub

La primera vez:

```powershell
git push -u origin nueva-rama
```

Después de esto, para futuros cambios de esta rama será suficiente con:

```powershell
git push
```

---

## 🔄 Resumen: nueva rama

```powershell
git switch main
git pull
git switch -c nombre-rama

# TRABAJAR EN EL CÓDIGO

git status
git add .
git commit -m "Descripción de los cambios"
git push -u origin nombre-rama
```

---

# 🔧 2. Modificar una rama existente

Utiliza este escenario cuando quieras **continuar trabajando en un programa que ya tiene su propia rama**.

### 1. Cambiar a la rama

```powershell
git switch nombre-rama
```

### 2. Actualizar la rama

```powershell
git pull
```

### 3. Trabajar en el código

Realiza tus modificaciones desde VS Code.

### 4. Comprobar los cambios

```powershell
git status
```

### 5. Preparar los cambios

```powershell
git add .
```

### 6. Crear un commit

```powershell
git commit -m "LO QUE SEA"
```

### 7. Subir los cambios

```powershell
git push
```

---

## 🔄 Resumen: modificar rama existente

```powershell
git switch nombre-rama
git pull

# TRABAJAR EN EL CÓDIGO

git status
git add .
git commit -m "Descripción de los cambios"
git push
```

---

# 🌳 3. Ver las ramas

Para ver las ramas locales:

```powershell
git branch
```

La rama en la que estás aparecerá con `*`.

Para ver también las ramas remotas:

```powershell
git branch -a
```

---

# 🔀 4. Cambiar entre ramas

Cambiar a `main`:

```powershell
git switch main
```

Cambiar a otra rama:

```powershell
git switch nombre-rama
```

---

# 🆕 5. Crear una rama desde la rama actual

```powershell
git switch -c nombre-rama
```

Ejemplo:

```powershell
git switch -c calculadora
```

> `-c` significa que Git crea la rama y te cambia a ella automáticamente.

---

# 📥 6. Descargar cambios de GitHub

Para actualizar la rama en la que estás:

```powershell
git pull
```

---

# 📤 7. Subir cambios a GitHub

Después de modificar el código:

```powershell
git add .
git commit -m "Descripción de los cambios"
git push
```

---

# 💾 8. Ver el historial de commits

```powershell
git log
```

Versión más compacta:

```powershell
git log --oneline
```

Ejemplo:

```text
a82f91c X1
3bc821a X2
7d21abc X3
```

---

# ⚠️ 9. Error: `src refspec main does not match any`

Si aparece:

```text
error: src refspec main does not match any
```

normalmente significa que todavía **no tienes ningún commit** en esa rama.

Solución:

```powershell
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

---

# 🧠 10. Comandos imprescindibles

| Comando               | Función                       |
| --------------------- | ----------------------------- |
| `git status`          | Ver el estado del repositorio |
| `git add .`           | Preparar todos los cambios    |
| `git commit -m "..."` | Crear un commit               |
| `git push`            | Subir cambios a GitHub        |
| `git pull`            | Descargar cambios de GitHub   |
| `git branch`          | Ver ramas                     |
| `git switch rama`     | Cambiar de rama               |
| `git switch -c rama`  | Crear y cambiar a una rama    |
| `git log --oneline`   | Ver historial resumido        |

---

# 🚀 Chuleta rápida

### Crear programa nuevo

```powershell
git switch main
git pull
git switch -c nombre-rama

# TRABAJAR

git add .
git commit -m "Añadir nuevo programa"
git push -u origin nombre-rama
```

### Continuar un programa existente

```powershell
git switch nombre-rama
git pull

# TRABAJAR

git add .
git commit -m "Actualizar programa"
git push
```

### Ver dónde estoy

```powershell
git branch
```

### Ver cambios

```powershell
git status
```

### Ver historial

```powershell
git log --oneline
```
