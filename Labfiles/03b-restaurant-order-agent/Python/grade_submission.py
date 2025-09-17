#!/usr/bin/env python3
"""
Restaurant Order AI Agent - Auto Grading Script
===============================================

This script automatically scores student submissions for the Azure DevOps work items
related to building a restaurant order management AI agent.

Usage:
    python grade_submission.py --student-dir ./student_submission --reference-dir ./reference_solution

Requirements:
    - Student's agent.py file
    - Student's user_functions.py file
    - Reference solution files (app_end.py, user_functions_end.py)
"""

import os
import sys
import ast
import json
import importlib.util
import tempfile
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Any
import argparse
from dataclasses import dataclass

@dataclass
class TestResult:
    """Represents the result of a single test"""
    work_item_id: str
    task_name: str
    passed: bool
    score: int
    max_score: int
    feedback: str
    details: List[str]

class AIAgentGrader:
    """Auto-grading system for Azure AI Agent assignments"""
    
    def __init__(self, student_dir: str, reference_dir: str):
        self.student_dir = Path(student_dir)
        self.reference_dir = Path(reference_dir)
        self.results: List[TestResult] = []
        self.total_score = 0
        self.max_total_score = 0
        
    def grade_submission(self) -> Dict[str, Any]:
        """Main grading function - returns comprehensive score report"""
        print("🎯 Starting Auto-Grader for Restaurant Order AI Agent")
        print("=" * 60)
        
        # Grade each Azure DevOps work item
        self._grade_pbi_045_infrastructure()
        self._grade_task_156_order_functions()
        self._grade_task_157_agent_configuration()
        self._grade_task_158_error_handling()
        self._grade_pbi_046_conversation_history()
        
        # Generate final report
        return self._generate_report()
    
    def _grade_pbi_045_infrastructure(self):
        """Grade PBI-2024-045: Azure AI Agent Infrastructure Setup"""
        print("\n📋 Grading PBI-2024-045: Infrastructure Setup...")
        
        result = TestResult(
            work_item_id="PBI-2024-045",
            task_name="Azure AI Agent Infrastructure Setup",
            passed=False,
            score=0,
            max_score=20,
            feedback="",
            details=[]
        )
        
        try:
            # Check if student file exists
            student_file = self.student_dir / "agent.py"
            if not student_file.exists():
                result.feedback = "❌ agent.py file not found"
                result.details.append("Missing agent.py file in submission")
                self.results.append(result)
                return
            
            # Parse student code
            with open(student_file, 'r', encoding='utf-8') as f:
                student_code = f.read()
            
            # Check imports
            import_score = self._check_imports(student_code)
            result.score += import_score
            result.details.append(f"Imports check: {import_score}/5 points")
            
            # Check Azure connection setup
            connection_score = self._check_azure_connection(student_code)
            result.score += connection_score
            result.details.append(f"Azure connection: {connection_score}/10 points")
            
            # Check environment variables
            env_score = self._check_environment_setup(student_code)
            result.score += env_score
            result.details.append(f"Environment setup: {env_score}/5 points")
            
            result.passed = result.score >= 15  # 75% threshold
            result.feedback = "✅ Infrastructure setup completed" if result.passed else "⚠️ Infrastructure setup needs work"
            
        except Exception as e:
            result.feedback = f"❌ Error grading infrastructure: {str(e)}"
            result.details.append(f"Exception: {str(e)}")
        
        self.results.append(result)
        self.total_score += result.score
        self.max_total_score += result.max_score
    
    def _grade_task_156_order_functions(self):
        """Grade TASK-2024-156: Implement Order Processing Functions"""
        print("\n🛠️ Grading TASK-2024-156: Order Processing Functions...")
        
        result = TestResult(
            work_item_id="TASK-2024-156",
            task_name="Order Processing Functions",
            passed=False,
            score=0,
            max_score=25,
            feedback="",
            details=[]
        )
        
        try:
            student_file = self.student_dir / "user_functions.py"
            if not student_file.exists():
                result.feedback = "❌ user_functions.py file not found"
                result.details.append("Missing user_functions.py file in submission")
                self.results.append(result)
                return
            
            # Test function implementations
            calc_score = self._test_calculate_order_total()
            result.score += calc_score
            result.details.append(f"calculate_order_total function: {calc_score}/10 points")
            
            process_score = self._test_process_restaurant_order()
            result.score += process_score
            result.details.append(f"process_restaurant_order function: {process_score}/10 points")
            
            functions_set_score = self._test_functions_set()
            result.score += functions_set_score
            result.details.append(f"user_functions set definition: {functions_set_score}/5 points")
            
            result.passed = result.score >= 20  # 80% threshold
            result.feedback = "✅ Order functions implemented correctly" if result.passed else "⚠️ Order functions need fixes"
            
        except Exception as e:
            result.feedback = f"❌ Error grading functions: {str(e)}"
            result.details.append(f"Exception: {str(e)}")
        
        self.results.append(result)
        self.total_score += result.score
        self.max_total_score += result.max_score
    
    def _grade_task_157_agent_configuration(self):
        """Grade TASK-2024-157: Configure AI Agent with Function Tools"""
        print("\n🤖 Grading TASK-2024-157: Agent Configuration...")
        
        result = TestResult(
            work_item_id="TASK-2024-157",
            task_name="AI Agent Configuration",
            passed=False,
            score=0,
            max_score=20,
            feedback="",
            details=[]
        )
        
        try:
            student_file = self.student_dir / "agent.py"
            with open(student_file, 'r', encoding='utf-8') as f:
                student_code = f.read()
            
            # Check FunctionTool and ToolSet usage
            toolset_score = self._check_toolset_configuration(student_code)
            result.score += toolset_score
            result.details.append(f"ToolSet configuration: {toolset_score}/8 points")
            
            # Check agent creation
            agent_score = self._check_agent_creation(student_code)
            result.score += agent_score
            result.details.append(f"Agent creation: {agent_score}/8 points")
            
            # Check thread management
            thread_score = self._check_thread_management(student_code)
            result.score += thread_score
            result.details.append(f"Thread management: {thread_score}/4 points")
            
            result.passed = result.score >= 16  # 80% threshold
            result.feedback = "✅ Agent configuration complete" if result.passed else "⚠️ Agent configuration incomplete"
            
        except Exception as e:
            result.feedback = f"❌ Error grading agent config: {str(e)}"
            result.details.append(f"Exception: {str(e)}")
        
        self.results.append(result)
        self.total_score += result.score
        self.max_total_score += result.max_score
    
    def _grade_task_158_error_handling(self):
        """Grade TASK-2024-158: Error Handling and Cleanup"""
        print("\n🛡️ Grading TASK-2024-158: Error Handling...")
        
        result = TestResult(
            work_item_id="TASK-2024-158",
            task_name="Error Handling and Cleanup",
            passed=False,
            score=0,
            max_score=15,
            feedback="",
            details=[]
        )
        
        try:
            student_file = self.student_dir / "agent.py"
            with open(student_file, 'r', encoding='utf-8') as f:
                student_code = f.read()
            
            # Check run status error handling
            error_check_score = self._check_run_status_handling(student_code)
            result.score += error_check_score
            result.details.append(f"Run status error handling: {error_check_score}/5 points")
            
            # Check cleanup implementation
            cleanup_score = self._check_cleanup_implementation(student_code)
            result.score += cleanup_score
            result.details.append(f"Resource cleanup: {cleanup_score}/5 points")
            
            # Check input validation
            validation_score = self._check_input_validation(student_code)
            result.score += validation_score
            result.details.append(f"Input validation: {validation_score}/5 points")
            
            result.passed = result.score >= 12  # 80% threshold
            result.feedback = "✅ Error handling implemented" if result.passed else "⚠️ Error handling needs improvement"
            
        except Exception as e:
            result.feedback = f"❌ Error grading error handling: {str(e)}"
            result.details.append(f"Exception: {str(e)}")
        
        self.results.append(result)
        self.total_score += result.score
        self.max_total_score += result.max_score
    
    def _grade_pbi_046_conversation_history(self):
        """Grade PBI-2024-046: Conversation History and Logging"""
        print("\n💬 Grading PBI-2024-046: Conversation History...")
        
        result = TestResult(
            work_item_id="PBI-2024-046",
            task_name="Conversation History and Logging",
            passed=False,
            score=0,
            max_score=20,
            feedback="",
            details=[]
        )
        
        try:
            student_file = self.student_dir / "agent.py"
            with open(student_file, 'r', encoding='utf-8') as f:
                student_code = f.read()
            
            # Check message retrieval
            message_score = self._check_message_retrieval(student_code)
            result.score += message_score
            result.details.append(f"Message retrieval: {message_score}/8 points")
            
            # Check conversation history display
            history_score = self._check_conversation_history(student_code)
            result.score += history_score
            result.details.append(f"History display: {history_score}/8 points")
            
            # Check message ordering
            ordering_score = self._check_message_ordering(student_code)
            result.score += ordering_score
            result.details.append(f"Message ordering: {ordering_score}/4 points")
            
            result.passed = result.score >= 16  # 80% threshold
            result.feedback = "✅ Conversation history complete" if result.passed else "⚠️ Conversation history incomplete"
            
        except Exception as e:
            result.feedback = f"❌ Error grading conversation history: {str(e)}"
            result.details.append(f"Exception: {str(e)}")
        
        self.results.append(result)
        self.total_score += result.score
        self.max_total_score += result.max_score
    
    # Helper methods for specific checks
    def _check_imports(self, code: str) -> int:
        """Check if required imports are present"""
        required_imports = [
            'DefaultAzureCredential',
            'AgentsClient', 
            'FunctionTool',
            'ToolSet',
            'MessageRole',
            'user_functions'
        ]
        
        score = 0
        for imp in required_imports:
            if imp in code:
                score += 1
        
        return min(score, 5)  # Max 5 points
    
    def _check_azure_connection(self, code: str) -> int:
        """Check Azure client connection setup"""
        score = 0
        
        if 'AgentsClient(' in code:
            score += 3
        if 'DefaultAzureCredential' in code:
            score += 3
        if 'exclude_environment_credential' in code:
            score += 2
        if 'exclude_managed_identity_credential' in code:
            score += 2
        
        return min(score, 10)
    
    def _check_environment_setup(self, code: str) -> int:
        """Check environment variable usage"""
        score = 0
        
        if 'load_dotenv()' in code:
            score += 2
        if 'PROJECT_ENDPOINT' in code:
            score += 2
        if 'MODEL_DEPLOYMENT_NAME' in code:
            score += 1
        
        return min(score, 5)
    
    def _test_calculate_order_total(self) -> int:
        """Test the calculate_order_total function"""
        try:
            # Import student's function
            spec = importlib.util.spec_from_file_location(
                "student_functions", 
                self.student_dir / "user_functions.py"
            )
            student_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(student_module)
            
            # Test function exists
            if not hasattr(student_module, 'calculate_order_total'):
                return 0
            
            func = student_module.calculate_order_total
            score = 0
            
            # Test with valid items
            try:
                result = func(['burger', 'fries'])
                if isinstance(result, str):
                    parsed = json.loads(result)
                    if 'total' in parsed and parsed['total'] == 17.98:
                        score += 5
                    if 'items' in parsed:
                        score += 3
            except:
                pass
            
            # Test with invalid items
            try:
                result = func(['invalid_item'])
                parsed = json.loads(result)
                if 'items' in parsed and len(parsed['items']) > 0:
                    score += 2
            except:
                pass
            
            return min(score, 10)
            
        except Exception:
            return 0
    
    def _test_process_restaurant_order(self) -> int:
        """Test the process_restaurant_order function"""
        try:
            spec = importlib.util.spec_from_file_location(
                "student_functions", 
                self.student_dir / "user_functions.py"
            )
            student_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(student_module)
            
            if not hasattr(student_module, 'process_restaurant_order'):
                return 0
            
            func = student_module.process_restaurant_order
            score = 0
            
            # Test function execution
            try:
                with tempfile.TemporaryDirectory() as temp_dir:
                    # Change to temp directory for file creation
                    original_cwd = os.getcwd()
                    os.chdir(temp_dir)
                    
                    result = func('John Doe', '555-1234', ['burger', 'soda'])
                    
                    if isinstance(result, str):
                        parsed = json.loads(result)
                        if 'message' in parsed:
                            score += 3
                        if 'order_number' in parsed:
                            score += 3
                        if 'total' in parsed:
                            score += 2
                    
                    # Check if file was created
                    order_files = [f for f in os.listdir('.') if f.startswith('order-')]
                    if order_files:
                        score += 2
                    
                    os.chdir(original_cwd)
            except:
                pass
            
            return min(score, 10)
            
        except Exception:
            return 0
    
    def _test_functions_set(self) -> int:
        """Test if user_functions set is properly defined"""
        try:
            spec = importlib.util.spec_from_file_location(
                "student_functions", 
                self.student_dir / "user_functions.py"
            )
            student_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(student_module)
            
            if not hasattr(student_module, 'user_functions'):
                return 0
            
            functions_set = student_module.user_functions
            score = 0
            
            if isinstance(functions_set, set):
                score += 2
            if len(functions_set) >= 2:
                score += 3
            
            return min(score, 5)
            
        except Exception:
            return 0
    
    def _check_toolset_configuration(self, code: str) -> int:
        """Check ToolSet and FunctionTool configuration"""
        score = 0
        
        if 'FunctionTool(' in code:
            score += 3
        if 'ToolSet()' in code:
            score += 2
        if 'toolset.add(' in code:
            score += 2
        if 'enable_auto_function_calls(' in code:
            score += 1
        
        return min(score, 8)
    
    def _check_agent_creation(self, code: str) -> int:
        """Check agent creation with proper parameters"""
        score = 0
        
        if 'create_agent(' in code:
            score += 3
        if 'name=' in code and 'restaurant' in code.lower():
            score += 2
        if 'instructions=' in code:
            score += 2
        if 'toolset=' in code:
            score += 1
        
        return min(score, 8)
    
    def _check_thread_management(self, code: str) -> int:
        """Check conversation thread management"""
        score = 0
        
        if 'threads.create()' in code:
            score += 2
        if 'create_and_process(' in code:
            score += 2
        
        return min(score, 4)
    
    def _check_run_status_handling(self, code: str) -> int:
        """Check run status error handling"""
        score = 0
        
        if 'run.status' in code:
            score += 2
        if 'failed' in code:
            score += 2
        if 'last_error' in code:
            score += 1
        
        return min(score, 5)
    
    def _check_cleanup_implementation(self, code: str) -> int:
        """Check resource cleanup"""
        score = 0
        
        if 'delete_agent(' in code:
            score += 3
        if 'agent.id' in code:
            score += 2
        
        return min(score, 5)
    
    def _check_input_validation(self, code: str) -> int:
        """Check input validation logic"""
        score = 0
        
        if 'len(user_prompt)' in code and '== 0' in code:
            score += 3
        if 'quit' in code.lower():
            score += 2
        
        return min(score, 5)
    
    def _check_message_retrieval(self, code: str) -> int:
        """Check message retrieval implementation"""
        score = 0
        
        if 'get_last_message_text_by_role(' in code:
            score += 4
        if 'MessageRole.AGENT' in code:
            score += 2
        if 'last_msg.text.value' in code:
            score += 2
        
        return min(score, 8)
    
    def _check_conversation_history(self, code: str) -> int:
        """Check conversation history display"""
        score = 0
        
        if 'messages.list(' in code:
            score += 3
        if 'ListSortOrder.ASCENDING' in code:
            score += 2
        if 'text_messages' in code:
            score += 2
        if 'message.role' in code:
            score += 1
        
        return min(score, 8)
    
    def _check_message_ordering(self, code: str) -> int:
        """Check proper message ordering"""
        score = 0
        
        if 'order=' in code:
            score += 2
        if 'ASCENDING' in code:
            score += 2
        
        return min(score, 4)
    
    def _generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive grading report"""
        
        percentage = (self.total_score / self.max_total_score * 100) if self.max_total_score > 0 else 0
        
        # Determine letter grade
        if percentage >= 90:
            letter_grade = "A"
        elif percentage >= 80:
            letter_grade = "B"
        elif percentage >= 70:
            letter_grade = "C"
        elif percentage >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
        
        report = {
            "overall_score": self.total_score,
            "max_score": self.max_total_score,
            "percentage": round(percentage, 1),
            "letter_grade": letter_grade,
            "passed": percentage >= 70,  # 70% passing threshold
            "work_items": []
        }
        
        # Add individual work item results
        for result in self.results:
            report["work_items"].append({
                "work_item_id": result.work_item_id,
                "task_name": result.task_name,
                "passed": result.passed,
                "score": result.score,
                "max_score": result.max_score,
                "percentage": round((result.score / result.max_score * 100), 1),
                "feedback": result.feedback,
                "details": result.details
            })
        
        return report
    
    def print_report(self, report: Dict[str, Any]):
        """Print formatted grading report"""
        print("\n" + "="*60)
        print("🎯 RESTAURANT ORDER AI AGENT - GRADING REPORT")
        print("="*60)
        
        print(f"\n📊 OVERALL RESULTS:")
        print(f"   Score: {report['overall_score']}/{report['max_score']} ({report['percentage']}%)")
        print(f"   Grade: {report['letter_grade']}")
        print(f"   Status: {'✅ PASSED' if report['passed'] else '❌ FAILED'}")
        
        print(f"\n📋 WORK ITEM BREAKDOWN:")
        for item in report['work_items']:
            status_icon = "✅" if item['passed'] else "❌"
            print(f"\n{status_icon} {item['work_item_id']}: {item['task_name']}")
            print(f"   Score: {item['score']}/{item['max_score']} ({item['percentage']}%)")
            print(f"   {item['feedback']}")
            for detail in item['details']:
                print(f"     • {detail}")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS:")
        failed_items = [item for item in report['work_items'] if not item['passed']]
        if failed_items:
            print("   Focus on improving these areas:")
            for item in failed_items:
                print(f"     • {item['work_item_id']}: {item['task_name']}")
        else:
            print("   Excellent work! All Azure DevOps work items completed successfully.")

def main():
    parser = argparse.ArgumentParser(description='Grade Restaurant Order AI Agent submissions')
    parser.add_argument('--student-dir', required=True, help='Path to student submission directory')
    parser.add_argument('--reference-dir', required=True, help='Path to reference solution directory')
    parser.add_argument('--output', help='Output file for JSON report (optional)')
    
    args = parser.parse_args()
    
    # Validate directories
    if not Path(args.student_dir).exists():
        print(f"❌ Student directory not found: {args.student_dir}")
        sys.exit(1)
    
    if not Path(args.reference_dir).exists():
        print(f"❌ Reference directory not found: {args.reference_dir}")
        sys.exit(1)
    
    # Run grading
    grader = AIAgentGrader(args.student_dir, args.reference_dir)
    report = grader.grade_submission()
    grader.print_report(report)
    
    # Save JSON report if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n📄 Detailed report saved to: {args.output}")

if __name__ == "__main__":
    main()