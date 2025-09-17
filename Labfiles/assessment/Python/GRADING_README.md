# Auto-Grading System for Restaurant Order AI Agent

## Overview

This auto-grading system evaluates student submissions for the Azure DevOps work items related to building a restaurant order management AI agent. It provides comprehensive scoring and feedback aligned with the specific tasks outlined in the Azure DevOps backlog.

## 🎯 What Gets Graded

### Azure DevOps Work Items Covered:

1. **PBI-2024-045: Infrastructure Setup** (20 points)
   - Azure AI SDK imports
   - Azure client connection 
   - Environment configuration

2. **TASK-2024-156: Order Processing Functions** (25 points)
   - `calculate_order_total()` implementation
   - `process_restaurant_order()` implementation
   - `user_functions` set definition

3. **TASK-2024-157: Agent Configuration** (20 points)
   - FunctionTool and ToolSet setup
   - Agent creation with proper parameters
   - Thread management

4. **TASK-2024-158: Error Handling** (15 points)
   - Run status error checking
   - Resource cleanup implementation
   - Input validation

5. **PBI-2024-046: Conversation History** (20 points)
   - Message retrieval
   - History display formatting
   - Chronological ordering

**Total: 100 points**

## 📋 Usage

### Basic Usage:
```bash
python grade_submission.py --student-dir ./student_submission --reference-dir ./reference_solution
```

### With JSON Output:
```bash
python grade_submission.py --student-dir ./student_submission --reference-dir ./reference_solution --output grade_report.json
```

### Test the Grader:
```bash
python test_grader.py
```

## 📁 Required File Structure

### Student Submission Directory:
```
student_submission/
├── agent.py           # Main agent implementation
└── user_functions.py  # Custom function implementations
```

### Reference Solution Directory:
```
reference_solution/
├── app_end.py              # Complete agent implementation
└── user_functions_end.py   # Complete function implementations
```

## 🔍 Grading Criteria

### Function Implementation Tests:

**calculate_order_total():**
- ✅ Function exists and is callable
- ✅ Correctly calculates totals from menu items
- ✅ Returns properly formatted JSON
- ✅ Handles invalid menu items gracefully

**process_restaurant_order():**
- ✅ Function exists with correct parameters
- ✅ Generates unique order numbers
- ✅ Creates order files on filesystem
- ✅ Returns JSON confirmation with order details

### Code Analysis Checks:

**Imports & Setup:**
- Required Azure AI SDK classes imported
- DefaultAzureCredential configuration
- Environment variables properly loaded

**Agent Configuration:**
- FunctionTool created from user functions
- ToolSet properly configured and enabled
- Agent created with appropriate instructions
- Conversation threads managed correctly

**Error Handling:**
- Run status checked for failures
- Agent resources properly cleaned up
- User input validated appropriately

**Conversation Management:**
- Messages retrieved using correct methods
- Conversation history displayed chronologically
- Message roles properly identified

## 📊 Scoring System

### Grade Scale:
- **A (90-100%):** All work items completed excellently
- **B (80-89%):** Most work items completed well
- **C (70-79%):** Basic requirements met (passing)
- **D (60-69%):** Some functionality implemented
- **F (0-59%):** Major functionality missing

### Passing Threshold:
- **Overall:** 70% (70/100 points)
- **Individual Work Items:** 75-80% depending on complexity

## 🧪 Example Output

```
🎯 RESTAURANT ORDER AI AGENT - GRADING REPORT
============================================================

📊 OVERALL RESULTS:
   Score: 78/100 (78.0%)
   Grade: C
   Status: ✅ PASSED

📋 WORK ITEM BREAKDOWN:

✅ PBI-2024-045: Azure AI Agent Infrastructure Setup
   Score: 18/20 (90.0%)
   ✅ Infrastructure setup completed
     • Imports check: 5/5 points
     • Azure connection: 8/10 points
     • Environment setup: 5/5 points

✅ TASK-2024-156: Order Processing Functions
   Score: 20/25 (80.0%)
   ✅ Order functions implemented correctly
     • calculate_order_total function: 10/10 points
     • process_restaurant_order function: 7/10 points
     • user_functions set definition: 3/5 points

❌ TASK-2024-158: Error Handling and Cleanup
   Score: 8/15 (53.3%)
   ⚠️ Error handling needs improvement
     • Run status error handling: 0/5 points
     • Resource cleanup: 5/5 points
     • Input validation: 3/5 points
```

## 🛠️ Customization

### Adjusting Point Values:
Modify the `max_score` values in each grading method:

```python
def _grade_pbi_045_infrastructure(self):
    result = TestResult(
        work_item_id="PBI-2024-045",
        task_name="Azure AI Agent Infrastructure Setup",
        max_score=25,  # Increase from 20 to 25
        # ... rest of implementation
    )
```

### Adding New Test Cases:
Extend the helper methods to check for additional requirements:

```python
def _check_custom_requirement(self, code: str) -> int:
    """Check for custom implementation requirement"""
    score = 0
    if 'custom_pattern' in code:
        score += 5
    return score
```

### Modifying Passing Thresholds:
Update the threshold values in individual grading methods:

```python
result.passed = result.score >= 18  # Change from 15 to 18 (90% instead of 75%)
```

## 🚀 Integration with Learning Management Systems

The grader outputs structured JSON that can be integrated with:
- Canvas API for gradebook updates
- Blackboard REST API
- Azure DevOps API for work item updates
- Custom learning platforms

### Sample JSON Output:
```json
{
  "overall_score": 78,
  "max_score": 100,
  "percentage": 78.0,
  "letter_grade": "C",
  "passed": true,
  "work_items": [
    {
      "work_item_id": "PBI-2024-045",
      "task_name": "Azure AI Agent Infrastructure Setup",
      "passed": true,
      "score": 18,
      "max_score": 20,
      "percentage": 90.0,
      "feedback": "✅ Infrastructure setup completed",
      "details": [
        "Imports check: 5/5 points",
        "Azure connection: 8/10 points"
      ]
    }
  ]
}
```

## 🔧 Troubleshooting

### Common Issues:

**ImportError during function testing:**
- Ensure student submission has valid Python syntax
- Check that required dependencies are available
- Verify file paths are correct

**FileNotFoundError:**
- Confirm student and reference directories exist
- Check file naming conventions match expected patterns

**Grading inconsistencies:**
- Review the specific test methods for accuracy
- Ensure reference solution follows the same patterns expected from students
- Update test criteria based on actual student submissions

This auto-grader provides comprehensive evaluation while maintaining alignment with the Azure DevOps work item structure, making it easy for instructors to provide meaningful feedback to students.