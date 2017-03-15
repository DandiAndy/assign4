JFLAGS	=	-g
JC	=	javac
.SUFFIXES:	.java	.class
.java.class:
	$(JC)	$(JFLAGS)	$*.java

CLASSES	=	\
	DT/ComparatorDescending.java	\
	DT/Util.java	\
	DT/Predict.java	\
	DT/Transaction.java	\
	DT/TransactionEntity.java	\
	DT/ID3.java

default:	classes

classes:	$(CLASSES:.java=.class)

clean:
		$(RM)	*.class
