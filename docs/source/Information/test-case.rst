@TestCase
*********
Annotation @TestCase is used to mark java class as a test case. 

.. csv-table:: 
	:header: Attribute, Description, Mandatory/Optional, Default Value
	:widths: 15, 40, 25, 20
	:stub-columns: 0
	
	skip(), Skip or Keep, Optional, false
	sequence(), Test sequence number, Optional, 0
	bugref(), Bug rReference, Optional, Empty String
	dropRemainingTestsUponFailure(), Trigger to drop remaining test cases from the execution list, Optional, false

..

* skip() 
	* Removes test case from execution list, skipped test case will not appear in GUI test selector.
	* Skip attribute will be applied regardless of test execution method (test list, test script or test scanning).
* sequence()
	* Provides sequence number to a test case. 
	* Test case(s) are assigned sequence number '0' if no sequence number is specified by the user.
	* Sequence number is ignored in case of test sequence is provided by the user (via test script or test list).
	* In absence of user provided test sequence (empty test list in the test-script or empty/null test list), test case execution sequence will be decided by first sorting packages by name in ascending order and secondly bubble sorting test cases using sequence number within their respective packages.
	* Test cases are sorted using bubble sort mechanism so any test case(s) (within same package) with same sequence number will be arranged as per their scan order, thus between them order of execution cannot be guaranteed.

	.. image:: Sort_Order.png
	
* bugref()
	* User can define bug reference (up to 20 bytes long)
* dropRemainingTestsUponFailure()
	* Enables dropping of remaining test cases from execution list if annotated test case fails. 

Annotation use case(s)
######################

.. code-block:: Java
	:linenos:
	:emphasize-lines: 0

	@TestCase(skip = false, sequence = 1, bugref = "JIRA-1234, JIRA-234", dropRemainingTestsUponFailure = true)

..

Example test case
#################

.. code-block:: Java
	:linenos:
	:emphasize-lines: 0

	import com.artos.annotation.TestCase;
	import com.artos.annotation.TestPlan;
	import com.artos.framework.infra.TestContext;
	import com.artos.interfaces.TestExecutable;

	@TestCase(skip = false, sequence = 1, bugref = "JIRA-1234, JIRA-234", dropRemainingTestsUponFailure = true)
	public class TestCase_1 implements TestExecutable {

	}

..