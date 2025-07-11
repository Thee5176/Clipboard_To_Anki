# Lessons Learned from Building Clipboard-to-Anki

## 1. **Overview**

- **Project Name**: Clipboard to Anki
- **Purpose**: lightweight command-line tool that automatically reads Japanese kanji from your clipboard, retrieves furigana (reading) and English translations, and saves them as a CSV file for easy Anki import. Just copy any Japanese text, run the program, and it generates ready-to-use flashcards—no manual input needed. Perfect for efficient language learning!
- **Technologies Used**:
  - Python
  - PyPl : pyperclip, pykakasi, deep-translation
- **Source of Motivation**:
  - Test Driven Development(TDD) -> The Clean Coder
  - UML -> personal interest

---

## 2. **Key Skills and Knowledge Acquired**

### **Programming/Technical Concepts**

- Object-oriented design: Learned how to design program into independent classes that has its own responsibility, the relationship between classes.
- UML diagram: First Implication of UML's Object diagram (class components and relationship link)

### **Frameworks/Tools**

- csv: Learned to use Python's `csv` module to export data.
- time: Learned to use Python's `time` module to slow down the loop
- 3rd party library: Gained confidence using library services that already built upon the real API call.

### **Debugging & Problem-Solving**

- test code with external library: Use `mock.patch()` function/class in unittest that redirect that function and inject with designated result
- unrelated object between Deck and FileHandler: Fix `__init__()` function that takes parent class as an instance

---

## 3. **Challenges Encountered**

### **Technical Challenges**

- testing tool & strategy: Struggled with mocking `pykakasi` instance methods and `deep-translate` instance class but resolved it by targeting the correct path.

### **Personal Challenges**

- Over-Specification : Balancing between features and time/knowledges required to build the project
- Premature Quitting : Overcoming procrastination when debugging complex issues.

---

## 4. **Improvements to Make in Future Projects**

- **Code Organization**: Refactor the code into smaller, reusable modules for better maintainability.
- **Testing**: Write more comprehensive unit tests to cover edge cases.
- **Performance**: -Not for now-

---

## 5. **Reflection**

- **What Went Well**: [E.g., "Successfully implemented CSV export with tag formatting and avoided data inconsistencies."]
- **What Could Have Gone Better**: Spent too much time debugging due to lack of fundamental concept fluency
- **Biggest Takeaway**: Start with clear data flow designs to avoid shared state issues.

---

## 6. **Additional Notes**

- This project highlight importance of foundational programming concepts. (not only grasp but require the fluency)

---

## 7. **Next Steps**

- GCP translation service

---

## 8. **Resources Used**

- [UML Diagrams](https://www.geeksforgeeks.org/unified-modeling-language-uml-introduction/): General knowledge of UML
- [UML Relationship](https://www.umlboard.com/docs/relations/): Six different type of class relations
- [Python| CSV doc](https://docs.python.org/3/library/csv.html#csv.writer): Guide on writing csv file with Python.
- [Python| with statement](https://realpython.com/python-with-statement/): Review Context Manager and `with` statement
