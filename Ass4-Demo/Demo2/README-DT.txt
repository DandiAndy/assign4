---------------------------------------------------------------------------------------------
This is an example of ID3 Decision Tree implementation in Java. 
Author: ...
---------------------------------------------------------------------------------------------

-What is this program for?

	This program is an implementation of ID3 algorithm to do the classification. It is coded in Java, and it is runnable on the server "bluenose.cs.dal.ca" with j2sdk 1.4.2. 

-How to run the program:
	a) run using make file:
	Place the input file (e.g., data1) in the root assignment directory (assign4)
	Copy the package folder "DT" under "assign4". Now all source files are under the package folder "DT"
	From the "assign4" folder compile the source files by "make"
	From the "assign4" folder run the executable program by "java DT.ID3" 

	Demo Example:
	...
	~/assign4$ java DT.ID3
	What is the name of the file containing your data?
	data1
	Please choose an attribute (by number):
			1. Humidity
			2. Windy
			3. PlayTennis
	Attribute: 3
	Target attribute is: PlayTennis

	if outlook is sunny, then
			if Humidity is high, then PlayTennis is N.
			if Humidity is normal, then PlayTennis is P.
	if outlook is overcast, then PlayTennis is P.
	if outlook is rain, then
			if Windy is false, then PlayTennis is P.
			if Windy is true, then PlayTennis is N.
	rakib@bluenose:~/assign4$
	
	b) run without make file:
	Place the input file in the root assignment directory (assign4)
	Copy the package folder "DT" under "assign4". Now all source files are under the package folder "DT"
	From the "assign4" folder compile the source files by "javac DT/*.java" 
	From the "assign4" folder run the executable program by "java DT.ID3" 
	
	Demo example: 
	~/assign4$ javac DT/*.java
	~/assign4$ java DT.ID3
	What is the name of the file containing your data?
	data1
	Please choose an attribute (by number):
			1. Humidity
			2. Windy
			3. PlayTennis
	Attribute: 3

	
- Assumptions on Data Preprocessing
	1. The database file is space delimited. (e.g. "North America" is not allowed. Instead of that "North_America" is ok)
	2. The target attribute must have the values of two class labels (e.g., PlayTennis=yes or PlayTennis=no)
	3. Missing value should be represented as empty string (e.g., space)

- Assumptions on Stopping Condition
	1. When no sample is left to build DT
	2. When all values of the target attribute are same for a set of samples (e.g., PlayTennis= either all yes or all no)
	3. When no attribute is left (e.g., run out of attributes) while building the ID3 decision tree and still the values in the subset are not in the same class, apply the following:
		2.1 Use majority voting to determine the class of prediction.
		2.2 If there is a tie (e.g., number of yes and no are same, then go to the parent subset until the tie breaks)
	4. If there is noisy/fuzzy subset of samples (e.g., there are different labels for all samples where each row is same)
		outlook  temperature    humidity   class
		------    ---------     --------   -----  
		rain     cool            normal      no
		rain     cool            normal      yes
	   Then, choose the first value for the class label (e.g, "no" for the above case)	

   
- Overview of the program code:

The assignment contains the "DT" package folder having the complete solution and can be opened in Eclipse. It contains following files with functions.

There are 6 files with mentioned main functions

File Name					Function Names                                    
===============================================================================================
1. ComparatorDescending.java					
					public ComparatorDescending(Map<String, Integer> map)
					public int compare(Object o1, Object o2)
				
2. ID3.java
					public static void main(String[] args)
					private String getInputFile(BufferedReader br)
					private String getPredictionColumn(LinkedHashMap<String,Integer> bAttributeNameIndex, BufferedReader 
						br)	

3. Predict.java
					public Predict(TransactionEntity objET)
					public void GenerateDT(ArrayList<ArrayList<String>> transactions, ArrayList<String> rules)
					private double computeEntropyOnTheSamples(ArrayList<String> targetLabels)
					private ArrayList<String> getTargetClassLabels(ArrayList<ArrayList<String>> transactions)
					private LinkedHashMap<String, Integer> getLabelCount (ArrayList<String> targetLabels)
					private int getSplitAttributeIndex(ArrayList<ArrayList<String>> transactions, double entropy)
					private double computeGainOnEachAttribute(LinkedHashMap<String, ArrayList<String>> 
						hmAttrValueToClassValues, double entropy, int totalSamples)
					private LinkedHashMap<String, ArrayList<ArrayList<String>>> getSubsets(int splitAttributeIndex,
						ArrayList<ArrayList<String>> transactions)
					private boolean outOfAttributes(ArrayList<ArrayList<String>> transactions)
					private String getMajorityLabel(Stack<ArrayList<String>> stLabels)
					private Map<String, Integer> sortHashMap(LinkedHashMap<String, Integer> hmCount)
					private void printRule(String key, ArrayList<String> rules)
					private void printRule(String key)
						
4. Transaction.java
					public TransactionEntity loadTransactionFile(String transactionFilePath)

5. TransactionEntity.java
					public TransactionEntity(): Structure class for transaction DB: ArrayList<ArrayList<String>> transactions, LinkedHashMap<String, String> itemCodes, ArrayList<String> columnNames.
					

6. Util.java
					public LinkedHashMap<String,Integer> getBinaryAttributes(TransactionEntity objET)
					public TransactionEntity reorderTransactions(TransactionEntity objET, int targetIndex)
	
- Description about some core methods
	GenerateDT(): it contains the main process of ID3 algorithm. It is a recursive function to build the decision tree.
	computeEntropyOnTheSamples(): It computes entropy using the target class labels within a subset of samples.
	getSplitAttributeIndex(): It gives the index of the attribute based on which the subset of samples will be split
	computeGainOnEachAttribute(): It computes the information gain on each each attribute within the subset of samples
	getSubsets(): It extracts the subset of samples
	outOfAttributes(): It checks whether the subset is out of attribute or not.
	getMajorityLabel(): It uses the majority voting mechanism to assign a class label
	loadTransactionFile(): It performs preprocessing on the data and loads the transaction file into memory
	getBinaryAttributes(): It selects the attributes for prediction	that have values of two different class labels (e.g., 
							PlayTennis=yes or PlayTennis=no)

- The program flow 
	main() --> load data 
		--> print out all binary attributes
		--> call GenerateDT()
		--> print rules while building the Tree
							
- All functions and classes are commented in the code

