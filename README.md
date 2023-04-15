# Evaluation of the incidence of serum cholesterol levels (mg/dl) on blood pressure levels (mm Hg) in older men in transition to old age (60-65 years) with coronary disease.
## Research question: What is the relationship between serum cholesterol levels (mg/dl) over blood pressure levels (mm Hg) in older men transitioning to old age (60-65 years) with coronary heart disease? in Cleveland?
## Introduction
Death from cardiovascular diseases represents the greatest cause of human deaths throughout the world, only in 2015 the World Organization for Health recorded that there were 17.7 million deaths from this cause, which would represent a 31% of the total deaths, within which we can highlight coronary disease covers the main deadly cardiovascular disease registering 7.4 million deaths to its cause, in the same way it has been considered that the people closest to 65 years of age are more prone to perish from said disease in the same way as subjects with poor quality of life, which includes a poor diet and a sedentary life. </br>
For this reason it is has been selected to carry out a study that would start from information extracted from a database of data published in 1988 by V.A. Medical Center, Long Beach and the Clinic Foundation of Cleveland regarding medical charts of subjects with coronary disease, for said reason is that taking into account certain studies that relate serum cholesterol levels with resting blood pressure such as the study titled “Low Levels of Low-Density Lipoprotein Cholesterol and Blood Pressure and Progression of Coronary Atherosclerosis” (Chhatriwalla, 2009), it has been decided to determine the existing correlation between both variables taking into account subjects from Cleveland with ages close to 65 years (60-65 years) who have coronary disease and belong to the masculine gender to avoid abounding in menopausal or hormonal issues resulting from it so that it focuses on the evaluation of the correlation in order to empirically determine said approach.
### General objective 
The aim of this experiment is to determine and interpret the correlation and causality between serum cholesterol levels (mg/dl) and resting blood pressure (mm Hg) in a population of men in transition to the third age (60-65 years) with coronary heart disease in Cleveland.
### Prediction
There is a positive correlation greater than 0.5 between serum cholesterol levels and resting blood pressure in the sample group because high serum cholesterol levels are highly considered as triggers of coronary disease due to obstruction of the blood duct of the coronary artery by the formation of clumps of fat on the intravenous walls (Chhatriwalla, 2009).
### Definition of variables
For the development of the research, 5 variables have been selected, which are:
#### Independent variables:
● Cholesterol levels (mg/dl) (precision ±2 mg/dl)
#### Constant Variables:

● Sex (male) Tools </br>
● Age (60-65 years) </br>
● Conditions (Coronary Disease) </br>

#### Dependent Variables:
● Resting blood pressure (mm Hg) (accuracy ±3 mmHg)

### Tools
● Jupyter Lab programming environment. </br>
● Python 2.4 computer programming language. </br> 
● Computer library: Spicy, Pandas, Numpy, Matplotlib, Seaborn. </br>

Tools used by the authors of the database to carry out measurements:

● Blood pressure meter (±3 mm Hg) </br>
● Serum cholesterol meter (±2 mg/dl) </br>

## Data collection and preprocessing
All the samples were obtained from the Cleveland coronary disease database published in 1987 in the UCI Machine Learning digital repository, which contains information on 14 different variables related to 270 subjects with coronary disease from that city. However, due to the diversity of data found, the following selection criteria have been applied.

● Contain numerical values of the variables: age, serum cholesterol and blood pressure at rest. </br>
● That the gender of the patient is male. </br>
● That the age variable encompasses a range between 60 and 65 years. </br>
● That the values obtained are within a percentile between 5% and 95% of the data collected from the age range. </br>

For this data preprocessing, it has been decided to use the Jupyter programming environment of the Python programming language, so that its implementation and the generated code can be seen in the annexes section.

## Results
● Number of samples after applying ranges = 29/270 </br>
● Number of samples after applying percentiles and eliminating missing = 19/270 </br>
● Total number of samples after preprocessing = 19/270 = 0.7% </br>

Once the variables have been preprocessed, the application of the relationship evaluation method that both variables could present by means of Pearson's correlation coefficient has been carried out in order to interpret their causality by means of a theoretical analysis. This is how the corresponding null and alternative hypotheses have been proposed.

Alternative hypothesis: There is a high correlation between cholesterol levels (mg/dl) on blood pressure (mm Hg) in men in middle adulthood (60-65 years) with coronary disease.

Null hypothesis: There is no correlation between cholesterol levels (mg/dl) on blood pressure levels (mm Hg) in men in middle adulthood (60-65 years) with coronary disease.

Given the hypotheses, it can be considered that the alternative hypothesis could be approved and the hypothesis rejected if there is a Pearson correlation coefficient greater than 0.5 or less than -0.5, and on the contrary, the null hypothesis could be approved and
reject the alternative hypothesis in case there is a correlation with a range between -0.5 and 0.5.

In this way, the method could be carried out from the results obtained in the data processing that can be seen in Table 1.

##### Table 1
Table of Serum Cholesterol levels (± 2 mg/dl) and Resting Blood Pressure (±3 mm Hg) of men between 60 and 65 years of age in Cleveland and their necessary values for the application of methodologies

![cheese](https://github.com/Mihail-Zuniga/Evaluation-of-correlation-between-cholesterol-and-blood-preasure/blob/main/graphs/Captura%20web_15-4-2023_15627_.jpeg)
Note. Own authorship.

From Table 1, information can be extracted to carry out the determination of the Pearson's correlation coefficient from the following formula: </br>
![cheese](https://github.com/Mihail-Zuniga/Evaluation-of-correlation-between-cholesterol-and-blood-preasure/blob/main/graphs/Captura%20web_15-4-2023_15352_.jpeg) </br>

Established said Pearson Correlation Coefficient, it can be denoted that it is within the range closest to zero (-0.5 < r < 0.5) in such a way that it can be considered that there is no correlation between the levels of serum Cholesterol and Blood Pressure at rest within the sample group.
In the same way, it can be considered from the results obtained that express that there is no correlation between the selected variables, the null hypothesis can be approved while the alternative hypothesis can be refuted.
## Discussion
It can be considered that there is an almost zero correlation between the variables of Serum Cholesterol and Blood Pressure, mainly because although there is a causality between the levels of cholesterol in the blood, there are several other factors that are determinants for the levels of blood pressure in the blood system and it is that as in the case of subjects who have hypertension, it can be considered that there are a series of causes that could lead to said condition, as expressed by the Mayo Clinic Institute in July 2021, among these causes the following can be highlighted: </br>


● Age: In those with an age close to 65 years, they usually present frequently (60%-70%) cases of high isolated systolic hypertension due to arterial stiffness generated by the loss of elasticity, which promotes that they can be easily blocked or rupture. Thus, causing complications such as: angina, myocardial infarction, heart failure, stroke and kidney failure (Osakidetza, 2022). Those changes produced in the blood vessels by age are that the baroreceptors that are responsible for controlling blood pressure lose sensitivity with old age, another aspect related to age that would trigger high blood pressure is that the capillaries tend to thicken, in such a way that a slower rate of nutrient exchange is generated. Consequently, another consequence could be that the aortic artery tends to become thicker, stiffer and more sensitive due to changes in the connective tissue of the blood vessel wall, causing a thickening of the myocardium and other arteries such as the coronary artery as well. may undergo this change, which would stand out due to the emphasis of the group of participants who already had coronary disease. As a final aspect, it can be noted that due to old age the amount of body water is reduced and with it the blood volume also decreases, therefore a greater pressure is needed for the individual's blood supply. For this reason it can be noted that one of the most influencing factors on blood pressure levels is age, since a range of subjects (60-65 years) has been selected that is considered as transitory to the elderly It can be denoted that it can be a cause of serum cholesterol levels having a minimal relationship compared to age. </br>

● Family history: It can be considered that arterial hypertension is a disease with a hereditary pattern of complex traits (non-Mendelian inheritance), multifactorial and polygenic, therefore, the expression of these genes can be intensified by environmental risk factors and other susceptibilities. genetic, this is how studies suggest that genetic risk means 30% - 40% of the variation in blood pressure of individuals (Valdés, 2013). </br>

● Overweight or obesity: It has been considered that obesity and overweight as a cause and form of coronary disease contribute to an increase in the blood pressure levels because it entails insulin resistance as well as an increase in adrenergic and aldosterone activity, in the same way as an increase in cardiac output and being linked to endothelial alteration through adiponectin or leptin molecules (López, 2004), for this reason it can be considered that obesity is a fundamental factor for obtaining a blood pressure.
high blood pressure and considering the city of Cleveland as a central city, it can be linked to a sedentary life on the part of its inhabitants, in this way it can be highlighted that there would be a considerable number of people in said state of health and taking into account another factor that is that these subjects have coronary disease, something that would be directly linked to diseases such as being overweight. </br>

● Stress: It can be considered that there is a possible relationship still under study that links the levels of stress and high blood pressure, mainly due to the actions that it leads to in individuals, which are usually actions such as smoking, drinking alcohol in excess, eating food unhealthy, however, in addition to the reactions that can be had in the face of stress, it can be considered that there would be a relationship between stress and high blood pressure in the long term (Mayo Clinic, 2021), however, it can still be considered that it is a theory in the process of validation by the scientific community, but in the event that a causality did exist, it can be noted that within the case study, due to the urban condition of Cleveland, the presence of unhealthy foods and the consumption of substances such as alcohol or cigarettes. </br>

● Serum cholesterol: It can be considered that if serum cholesterol levels decrease, they lead to a decrease in the incidence of subjects with coronary disease, however, this relationship is also conferred with various other factors already mentioned, due to the fact that the group study has coronary disease, an important factor for its generation can be highlighted is cholesterol because high levels of it (hypercholesterolemia) promote the development of atherosclerosis, which is a phenomenon characterized by the accumulation of lipids in the the walls of the arteries, thus promoting an inflammatory reaction and the formation of an atheromatous plaque, this process can occur in the long term, which could mean that the study group could have generated coronary disease over time, in such a way so that despite no longer having high cholesterol they could present this problem due to its development in earlier times, however, this process can be influenced in the same way by factors such as hypertension, diabetes and smoking, in this way Thus, as the atheromatous plaque grows in size, the patient would obtain an obstruction of the blood channel and therefore the supply of blood and oxygen would be reduced, thus leading to coronary disease through the formation of angina in the chest and a possible increase in blood pressure, however, being seen as a factor that can vary in incidence according to other factors, in such a way that its influence can be overshadowed by said factors in such a way that an almost null correlation can be presented with respect to those variables (Cachofeiro, 2020). 
## Conclusions
● There is no correlation between serum cholesterol levels (mg/dl) and blood pressure (mm Hg) in Cleveland men ages 60 to 65 with coronary artery disease due to the increased incidence of external factors such as: previous development in the long term of coronary disease and high blood pressure, age, family history, overweight or obesity, stress and consumption of substances such as tobacco and alcohol, in addition the causality is considered to be reduced. </br>

● Blood pressure levels depend on a different number of factors depending on the age group of the sample, so that in adults in transition to the third age (60-65 years) who belong to a central city and have previous disease Coronary arterial pressure strongly  depends on the way of life and hereditary conditions of said patient.

## Considerations
From the present investigation, it should be considered that a reduced group of subjects of 19 people has been taken into account after data preprocessing, so that it is a small number to carry out a deep evaluation of correlation since the marked trend can become reduced. Finally, it can be taken into account that the group covered is specific and variations could be applied with respect to the selection of variables for the study so that the nature of coronary disease can be adequately understood, in addition it has focused on obtaining information from subjects more vulnerable to coronary disease based on scientific studies.
## References and bibliography
- Duque, C. (2007). Principios indemostrables y conocimiento en Aristóteles. Revista Filosofía
UIS, 6(1), 73-86. https://bit.ly/3CkTA6t
- Valdés, M. T. L., & Herrera, J. A. C. (2013). Estudios sobre las bases genéticas de la
hipertensión arterial. Revista Cubana de Investigaciones Biomédicas, 32(1).
https://bit.ly/3sQFQNv
- López de Fez, C. M., Gaztelu, M. T., Rubio, T., & Castaño, A. (2004, August). Mecanismos
de hipertensión en obesidad. In Anales del Sistema Sanitario de Navarra (Vol. 27, No.
2, pp. 211-219). Gobierno de Navarra. Departamento de Salud. https://bit.ly/3vNSaAc
- Chhatriwalla, A. K., Nicholls, S. J., Wang, T. H., Wolski, K., Sipahi, I., Crowe, T., ... &
Nissen, S. E. (2009). Low levels of low-density lipoprotein cholesterol and blood
pressure and progression of coronary atherosclerosis. Journal of the American
College of Cardiology, 53(13), 1110-1115. https://bit.ly/3KHOO67
- Organización Mundial de la Salud. (2021). Enfermedades cardiovasculares.
https://bit.ly/3ClCsNY
- Mayo Clinic (2021). El estrés y la presión arterial alta: ¿cuál es la conexión?.
https://mayocl.in/3IRvbI0
Osakitdetza. (2022). Hipertensión arterial en mayores de 65 años. https://bit.ly/3IZA564
- Cachofeiro, V. (2021). Alteraciones del colesterol y enfermedad cardiovascular (cap. 13).
FBBVA, pp. 131-132. https://bit.ly/3HRoZP0
