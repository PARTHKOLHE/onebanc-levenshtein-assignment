# OneBanc Levenshtein Distance Assignment

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)

Professional implementation of Levenshtein distance algorithms with spell checking functionality for OneBanc technical assessment.

## 🚀 Quick Results

### Assignment Test Cases

Task 1: EditDistance("kitten", "sitting") = 3 ✅
Task 1: EditDistance("flaw", "lawn") = 2 ✅
Task 1: EditDistance("algorithm", "logarithm") = 3 ✅

Task 2: WeightedDistance with Ci=1, Cd=2, Cs=3 ✅
Task 3: Spell Checker with custom costs ✅
Task 4: 99%+ space optimization achieved ✅

## 📦 Installation & Usage

Clone or download this repository
Navigate to the project directory
cd onebanc-levenshtein

Create virtual environment
python -m venv venv

Activate virtual environment (Windows)
venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Run the demonstration
python examples/demo.py

Run tests
pytest tests/ -v

## 📋 Project Structure

onebanc-levenshtein/
├── edit_distance/ # Main package
│ ├── core.py # Algorithm implementations
│ └── spell_checker.py # Spell checker functionality
├── tests/ # Comprehensive test suite
├── examples/ # Demonstration scripts
├── screenshots/ # Output screenshots
└── docs/ # Additional documentation

## 🔧 Implementation Details

### Task 1: Standard Levenshtein Distance

- **Algorithm**: Wagner-Fischer dynamic programming
- **Time Complexity**: O(m × n)
- **Space Complexity**: O(m × n)

### Task 2: Weighted Edit Distance

- **Features**: Custom costs for insertion, deletion, substitution
- **Validation**: Input validation and error handling

### Task 3: Spell Checker

- **Functionality**: Find words with minimum edit distance
- **Output**: List of suggestions and minimum distance

### Task 4: Space Optimization

- **Technique**: Rolling arrays to reduce space complexity
- **Improvement**: O(m × n) → O(min(m, n)) space
- **Performance**: Maintains O(m × n) time complexity

## 🧪 Testing

Comprehensive test suite includes:

- Assignment example test cases
- Edge case validation
- Mathematical property verification
- Performance benchmarking
- Optimization correctness checks

Run all tests
pytest tests/ -v

Run with coverage
pytest tests/ --cov=edit_distance --cov-report=html

## 🎯 Assignment Compliance

✅ **Task 1**: Standard Levenshtein distance implementation  
✅ **Task 2**: Weighted edit distance with custom costs  
✅ **Task 3**: Spell checker using edit distance  
✅ **Task 4**: Space optimization analysis and implementation  
✅ **Documentation**: Comprehensive README and code comments  
✅ **Testing**: Professional test suite with edge cases  
✅ **Code Quality**: Type hints, error handling, performance analysis

## 📊 Performance Analysis

| String Length | Standard Time | Optimized Time | Space Savings |
| ------------- | ------------- | -------------- | ------------- |
| 10×10         | 0.05ms        | 0.04ms         | 90%           |
| 50×50         | 1.2ms         | 1.1ms          | 98%           |
| 100×100       | 4.8ms         | 4.5ms          | 99%           |


## 📸 Screenshots

All outputs and code implementations are documented in the `screenshots/` folder:

- **Code Implementation**: Professional CodeSnap screenshots of all algorithm functions
- **Test Results**: Complete test suite execution showing 100% pass rate
- **Coverage Report**: Testing coverage analysis demonstrating thorough validation
- **Demo Output**: Full demonstration script execution (split across multiple images due to length)
- **HTML Coverage**: Optional browser-based coverage visualization


## 👨‍💻 Author

**Parth Kolhe**  
OneBanc Technical Assessment  
Date: 09/07/2025

## 📝 License

This project is created for OneBanc technical assessment purposes.
