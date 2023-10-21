## Prep
setwd('./')
hf=read.csv('HF_Model_Data.csv')
hf[hf=="N/A"]=NA

## Some data cleanup
hf$Creatinine<-as.numeric(hf$Creatinine)
hf$Ejection_Fraction<-as.numeric(hf$Ejection_Fraction)
hf$Ejection_Fraction[is.na(hf$Ejection_Fraction)] <- mean(hf$Ejection_Fraction, na.rm=TRUE)

# age class
hf$age_class <- cut(hf$Age, breaks = seq(10, 90, by=20))
hf$age_class_70 <- cut(hf$Age, breaks = c(-1, 70, 90))
hf$bp_use_class <- cut(hf$bp_count_relative, labels=c("very low", "low", "medium", "high"), 
                       breaks = c(-1, 0.03333, 0.43333, 1.1, 5))

# recategorize Race
race_class <- c('African-American'='African-American',
                'Asian Indian'='Other',
                'Chinese'='Other',
                'Other'='Other',
                'Ugandan'='Other', 
                'Unknown'=NA,
                'White'='White')
hf$Race_Sorted <- as.factor(race_class[hf$Race]) 

# recategorize Marital Status
marital_class <- c('Divorced'='Single',
                   'Married'='Not Single',
                   'Separated'='Single',
                   'Partner'='Not Single',
                   'Single'='Single',
                   'Unknown'=NA,
                   'Widowed'='Single')
hf$Marital_Sorted <- as.factor(marital_class[hf$Marital_Status_desc]) 

## Split into read and non_read dfs
split_df <- split(hf, hf$Readmission_Outcome)
hf_non_read <- split_df[[1]]
hf_read <- split_df[[2]]

sapply(hf_read, table)
sapply(hf_non_read, table)
sapply(hf_read, mean, na.rm=TRUE)
sapply(hf_read, sd, na.rm=TRUE)
sapply(hf_non_read, mean, na.rm=TRUE)
sapply(hf_non_read, sd, na.rm=TRUE)

summary(hf$bp_count_relative)
table(hf$bp_use_class, hf$age_class)
table(hf$bp_use_class, hf$age_class_70)

## some stats
chisq.test(hf$Race_Sorted, hf$Readmission_Outcome, correct=TRUE)
chisq.test(hf$Marital_Sorted, hf$Readmission_Outcome, correct=TRUE)
fisher.test(hf$Race_Sorted, hf$Readmission_Outcome)
fisher.test(hf$Marital_Sorted, hf$Readmission_Outcome)
fisher.test(hf$pci, hf$Readmission_Outcome)
fisher.test(hf$acei_arb, hf$Readmission_Outcome)
fisher.test(hf$bp_mean_k2, hf$Readmission_Outcome)
fisher.test(hf$bp_mean_k3, hf$Readmission_Outcome)
fisher.test(hf$bp_range_k2, hf$Readmission_Outcome)
fisher.test(hf$bp_range_k3, hf$Readmission_Outcome)
fisher.test(hf$bp_use_class, hf$age_class)
fisher.test(hf$bp_use_class, hf$age_class_70)
t.test(hf$weight_usage_relative~hf$Readmission_Outcome)
t.test(hf$bp_usage_relative~hf$Readmission_Outcome)
t.test(hf$dias_gr_90_percent~hf$Readmission_Outcome)
t.test(hf$sys_gr_140_percent~hf$Readmission_Outcome)
t.test(hf$max_weight~hf$Readmission_Outcome)
t.test(hf$min_weight~hf$Readmission_Outcome)
t.test(hf$min_weight~hf$Readmission_Outcome)
t.test(hf$wt_week1_count~hf$Readmission_Outcome)
t.test(hf$bp_week1_count~hf$Readmission_Outcome)
t.test(hf$wt_day_relative~hf$Readmission_Outcome)
t.test(hf$bp_day_relative~hf$Readmission_Outcome)
t.test(hf$bp_week1_count~hf$Readmission_Outcome)
t.test(hf$wt_week1_count~hf$Readmission_Outcome)
t.test(hf$device_days_relative~hf$Readmission_Outcome)

## Get odds ratios
loghf <- glm(formula=Readmission_Outcome~pci, data=hf, family=binomial)
summary(loghf)
exp(coef(loghf))

table(hf$pci, hf$Readmission_Outcome)




