
# Resumen de Automatización TPI

Este documento detalla la finalización de los casos de prueba de Interfaz de Usuario (UI) y de API para el Trabajo Práctico Integrador.

## 1. Tests de Interfaz de Usuario (SauceDemo)

**Archivos:** `cypress/e2e/caso1.cy.js`, `caso2.cy.js`, `caso3.cy.js`
**Reporte de Ejecución:** `mochawesome-report/final-report.html`

| Caso | Descripción | Estado |
| :--- | :--- | :--- |
| **Caso 1** | Logueo con diferentes usuarios y verificación de ordenamiento. | PASÓ |
| **Caso 2** | Logueo exitoso, ordenamiento y verificación de primer artículo. | PASÓ |
| **Caso 3** | Ciclo completo: Agregar, remover artículo y finalizar checkout. | PASÓ |

## 2. Tests de API (PokeAPI)

**Archivo:** `api-tests/api_tests.py`
**Herramienta:** Python (Librería `requests`)

| Caso | Endpoint | Descripción | Estado |
| :--- | :--- | :--- | :--- |
| **Caso 1** | `berry/1` | Verificación de `size`, `soil_dryness` y `firmness`. | PASÓ |
| **Caso 2** | `berry/2` | Verificación de `firmness` y comparación de `size` y `soil_dryness` con el Caso 1. | PASÓ |
| **Caso 3** | `pokemon/pikachu` | Verificación de `base_experience` (rango) y `type` (electric). | PASÓ |