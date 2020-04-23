This module implements the procedural generation of diseases, symptoms of diseases, as well as medications for the treatment of the disease.
Inside the solution, 3 text files with assets for procedural generation are embedded: list_name_illnesses.txt - file with the names of the diseases,
list_name_medicines.txt - a file with the names of medicines, list_name_symptoms.txt - a file with the names of symptoms. All asset names, except for symptoms, are fictitious.
If desired, they can be easily supplemented or replaced with your own.

The solution implements 3 independent classes: illness - disease, symptoms - symptoms, medicines - medicines.
Each of these classes implements class methods get_all_posible_name (cls) and init_group (cls, number).
The get_all_posible_name method performs the function of reading data from the asset file and prepares the data for further work.
The init_group (cls, number) method performs the function of initializing (creating) instances depending on the number of required objects. Names for instantiating the method selects
randomly from an array of prepared assets. When creating each of the instances, it is added to the list of created instances, which is located inside the class.

Instances of symptoms and medications are associated with instances of disease through aggregation. That is, each instance of the disease has a list of instances of symptoms and a list of lists of instances of medicines.

It is possible to ask an incompatible medication for any medication.

In the illness class, a method of the output_info_class (cls) class is implemented that displays information on the console about the name of the disease, its symptoms, and methods of treatment.
In the medicines class, this method displays the name of the medication and the name of the incompatible medication (if any).

Some auxiliary methods are also implemented for obtaining some data or manually setting / adding data, receiving all compatible medicines, receiving / adding incompatible medicines.

Instances, procedural generation, merging, and validation occur in the main.py file. All classes are imported into this file.

Generation proceeds as follows: in a conditional world n-random instances of symptoms are created from an asset file. Next, all possible non-recurring combinations of these symptoms are created.
Then n-random drug instances are created from the asset file. You can add an incompatible medication to a number of created medicines. All possible non-repeating combinations of these drugs are created without regard to incompatibilities. Further in the same way are created
n-random instances of diseases from the asset file. Checks are being carried out on the possibility of filling all copies of the disease with symptoms, medications. A random combination of symptoms is added,
medicines to a copy of the disease. When random combinations of medications are added, incorrect treatments are removed.

This generation can be used, for example, in some game projects. This will add to the project such a “feature” as replayability, since completely new diseases, symptoms and methods of their treatment will be created.

This procedural generation is just an example. It can be modified to suit your needs to everyone. For example, add a description of the disease to the disease class. To do this, you will have to come up with a description of each disease from the asset and, when generating, insert this description directly into the class.
Similarly, with medication and symptoms, you can give everyone a unique description and build into the class.
You can also redo the mechanism for specifying incompatibilities between medicines. For example, divide all medicines into groups, and create incompatibilities into groups, generating random / randoms incompatible groups at first.