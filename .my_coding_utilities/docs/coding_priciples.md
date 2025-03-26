### Codding Principles:
1. **Do Not Make Assumptions:**
   - If you need more details, ask the user
   - If you do not know, explain to the user that you could not find it.

2. **Single Responsibility Principle (SRP):**  
   - Ensure each class/method has one responsibility. Split any that do too much.

3. **Separation of Concerns (SoC):**  
   - Keep data access, business logic, and UI separated. Refactor if mixed.

4. **DRY (Don't Repeat Yourself):**  
   - Eliminate code repetition. Use reusable functions/classes for shared logic.

5. **Efficiency Review:**  
   - Review algorithms and data structures for bottlenecks and complexity.

6. **Code Formatting:**  
   - PEP 8: Follow PEP 8 style guidelines for consistent code formatting.
   - Type hints: Use type hints for improved code readability and error detection.
   - Importanize: Use Importanize for consistent import organization.
      - If you receive a "No module named 'imp'" error, read [importanize document](./importanize.md) 

7. **Code Organization:**  
   - Move code to the appropriate folder: 
     - **Configs:** settings, constants, etc.
     - **Controllers:** business logic
     - **User Interface:** UI elements only
     - **Utils:** utility functions 
   - Avoid mixing code types unless necessary.

8. **Documentation:**
   - Sphinx is installed and configured for documentation generation.

9. **Testing:**
   - Write unit tests for all new code