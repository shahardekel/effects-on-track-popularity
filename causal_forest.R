fact=function(treatment, df_path){
  path=paste(df_path,collapse="")
  data=read.csv(path)
  T=data[,treatment]
  Y=data[,"popularity"]
  drops<-c(treatment,"popularity")
  X=data[,!(names(data) %in% drops)]
  tau.forest = causal_forest(X, Y, T)
  return (average_treatment_effect(tau.forest, target.sample = "overlap"))
}

print("liveness")
print("df_ts1")
print(fact('liveness_binary',"/Users/shahardekel/PycharmProjects/CasualProject/df_ts1_prep.csv"))
print("df_ts3")
print(fact('liveness_binary',"/Users/shahardekel/PycharmProjects/CasualProject/df_ts3_prep.csv"))
print("df_ts4")
print(fact('liveness_binary',"/Users/shahardekel/PycharmProjects/CasualProject/df_ts4_prep.csv"))
print("df_ts5")
print(fact('liveness_binary',"/Users/shahardekel/PycharmProjects/CasualProject/df_ts5_prep.csv"))

print("-------------------------------")

print("danceability")
print("df_ts1")
print(fact('danceability_binary',"/Users/shahardekel/PycharmProjects/CasualProject/df_ts1_prep.csv"))
print("df_ts3")
print(fact('danceability_binary',"/Users/shahardekel/PycharmProjects/CasualProject/df_ts3_prep.csv"))
print("df_ts4")
print(fact('danceability_binary',"/Users/shahardekel/PycharmProjects/CasualProject/df_ts4_prep.csv"))
print("df_ts5")
print(fact('danceability_binary',"/Users/shahardekel/PycharmProjects/CasualProject/df_ts5_prep.csv"))

