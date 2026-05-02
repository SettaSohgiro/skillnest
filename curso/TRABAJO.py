
---

##  Desafío Final — Mini Sistema de Votación

 

Construye un programa que:

 

1. **Candidatos:** crea un diccionario con 4 candidatos y sus votos iniciales en 0:

   ```python

   candidatos = {"Alice": 0, "Bob": 0, "Carol": 0, "David": 0}

   ```

 

2. **Votación:** usa un `while` para recibir votos indefinidamente. En cada iteración:

   - Muestra los candidatos disponibles con sus votos actuales

   - Pide el nombre del candidato a votar

   - Si el nombre no existe → `"Candidato no encontrado"`

   - Si es válido → suma 1 voto

   - Si escribe `"fin"` → termina la votación

 

3. **Resultados:** al terminar, imprime:

   - Votos totales emitidos

   - Tabla de resultados con porcentaje de cada candidato

   - Ganador (si hay empate, muéstralo)

   - Barra de progreso ASCII para cada candidato

 

**Pista:** la barra puede ser así: `█████░░░░░ 5/10 votos (50%)`