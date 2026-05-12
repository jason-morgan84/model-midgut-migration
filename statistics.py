

# to do:
# use more efficient/simpler method of grouping (pandas data frames, groupby?)

import pandas as pd

df = pd.read_csv('output_short.csv')

df = df.sort_values(by = ['migration_speed','adhesion_force_pmec_multiple','internal_force','type','adhesion_force_other','repeat'])



df_all = df[df['type'] != "VM"].drop(['average_speed_total'], axis = 1)
df_all = df_all.set_index(['migration_speed','repeat','adhesion_force_pmec_multiple','internal_force','adhesion_force_other','type'])

df_wide = df_all.unstack('type').unstack('adhesion_force_other').unstack('repeat')

df_all_means = df_all.groupby(['migration_speed','adhesion_force_other','adhesion_force_pmec_multiple','internal_force','type']).agg(
    mean_speed_x = ('average_speed_x','mean'))

#df_all_means["ratio"] = df_all_means[1]/df_all_means[2]
df_all_means = df_all_means.unstack('type')
print(df_all_means.to_string())
#print(df_all_means['mean_speed_x'].to_string())

df_all_means = df_all_means.reset_index(['migration_speed','adhesion_force_other','adhesion_force_pmec_multiple','internal_force','mean_speed_x'])


print(df_all_means.to_string())
print(df_all_means.columns)
#print(df_wide.to_string())

#print(df_all_means.unstack('type').to_string())


#print(df_all_means['migration_speed'].to_string())
"""
class DataClass:
    def __init__ (self, migration_speed, adhesion_force_other, adhesion_force_pmec_multiple, internal_force, type, repeat, average_speed_x, average_speed_total):
        self.migration_speed = migration_speed
        self.adhesion_force_other = adhesion_force_other
        self.adhesion_force_pmec_multiple = adhesion_force_pmec_multiple
        self.internal_force = internal_force
        self.repeat = repeat
        self.type = type
        self.average_speed_x = average_speed_x
        self.average_speed_total = average_speed_total
    def __str__(self):
        return "\n".join(("migration_speed: " + str(self.migration_speed),
                    "adhesion_force_other: " + str(self.adhesion_force_other), 
                    "adhesion_force_pmec_multiple: " + str(self.adhesion_force_pmec_multiple),
                    "internal_force: " + str(self.internal_force), 
                    "type: " + self.type,
                    "repeat: " + str(self.repeat),
                    "average_speed_x: " + str(self.average_speed_x), 
                    "average_speed_total: " + str(self.average_speed_total)))
    def __repr__(self):
        return str(self)
    
    def parameters(self):
        return "\n".join(("migration_speed: " + str(self.migration_speed), 
                            "adhesion_force_pmec_multiple: " + str(self.adhesion_force_pmec_multiple),
                            "internal_force: " + str(self.internal_force)))
    
    def to_list(self):
        return [self.migration_speed, 
                self.adhesion_force_other,
                self.adhesion_force_pmec_multiple,
                self.internal_force,
                self.type,
                self.repeat,
                self.average_speed_x,
                self.average_speed_total]

file_name = "output.txt"

data = []
with open(file_name, "r") as input_file:
    input_file.readline()
    while line := input_file.readline():
        if len(line)>1:
            input = line.rstrip().split(" ")
            typed_input = []
            for item in input:
                try:
                    typed_input.append(float(item))
                except:
                    typed_input.append(item)
            typed_input[4], typed_input[5] = typed_input[5], typed_input[4]
            new_data = DataClass(*typed_input)
            data.append(new_data)


data.sort(key = lambda item: (item.migration_speed,
                              item.adhesion_force_other, 
                              item.adhesion_force_pmec_multiple,
                              item.internal_force,
                              item.type,
                              item.repeat))

#print(*data,sep='\n')

grouped_data=[]
for item in data:
    parameters = [item.migration_speed,
                    item.adhesion_force_other, 
                    item.adhesion_force_pmec_multiple,
                    item.internal_force,
                    item.type]
    if len(grouped_data) == 0:
        parameters.extend([[0],[round(item.average_speed_x,5)],[round(item.average_speed_total,5)]])
        grouped_data.append(DataClass(*parameters))
    else:
        new = True
        for n, grouped_item in enumerate(grouped_data):
            grouped_parameters = [grouped_item.migration_speed,
                                    grouped_item.adhesion_force_other, 
                                    grouped_item.adhesion_force_pmec_multiple,
                                    grouped_item.internal_force,
                                    grouped_item.type]
            if parameters == grouped_parameters:
                grouped_data[n].repeat.append(item.repeat)
                grouped_data[n].average_speed_x.append(round(item.average_speed_x,5))
                grouped_data[n].average_speed_total.append(round(item.average_speed_total,5))
                new = False
                break
        if new == True:
            parameters.extend([[0],[round(item.average_speed_x,5)],[round(item.average_speed_total,5)]])
            grouped_data.append(DataClass(*parameters))
        
data = grouped_data.copy()
grouped_data=[]

for item in data:
    parameters = [item.migration_speed,
                    item.adhesion_force_pmec_multiple,
                    item.internal_force,
                    item.type]
    
    if len(grouped_data) == 0:
        new_item = DataClass(*item.to_list())
        new_item.adhesion_force_other = []
        new_item.adhesion_force_other.append(item.adhesion_force_other)
        new_item.repeat = []
        new_item.repeat.append(item.repeat)
        new_item.average_speed_x = []
        new_item.average_speed_x.append(item.average_speed_x)
        new_item.average_speed_total = []
        new_item.average_speed_total.append(item.average_speed_total)
        grouped_data.append(new_item)
    else:
        new = True
        for n, grouped_item in enumerate(grouped_data):
            grouped_parameters = [grouped_item.migration_speed,
                                    grouped_item.adhesion_force_pmec_multiple,
                                    grouped_item.internal_force,
                                    grouped_item.type]
            if parameters == grouped_parameters:
                grouped_data[n].adhesion_force_other.append(item.adhesion_force_other)
                grouped_data[n].repeat.append(item.repeat)
                grouped_data[n].average_speed_x.append(item.average_speed_x)
                grouped_data[n].average_speed_total.append(item.average_speed_total)
                new = False
                break
        if new == True:
            new_item = DataClass(*item.to_list())
            new_item.adhesion_force_other = []
            new_item.adhesion_force_other.append(item.adhesion_force_other)
            new_item.repeat = []
            new_item.repeat.append(item.repeat)
            new_item.average_speed_x = []
            new_item.average_speed_x.append(item.average_speed_x)
            new_item.average_speed_total = []
            new_item.average_speed_total.append(item.average_speed_total)
            grouped_data.append(new_item)

#for item in grouped_data:
#    print(item.migration_speed, item.adhesion_force_pmec_multiple,item.internal_force,item.type,item.adhesion_force_other)


# for each item in the list
# ignoring first and last adhesion force
# go through each adhesion force check if the mean is greater than both the means of the adhesion forces on either side
# if it is, do a t-test, get p
# save values and p

from scipy import stats

parameters_of_interest = []
critical_p_val = 0.2


for item in grouped_data:
    if item.type == "Other":
        for n, adhesion in enumerate(item.adhesion_force_other):
            if n > 0 and n < len(item.adhesion_force_other) - 1:
                mean = sum(item.average_speed_x[n]) / len(item.average_speed_x[n])
                next_mean = sum(item.average_speed_x[n + 1]) / len(item.average_speed_x[n + 1])
                previous_mean = sum(item.average_speed_x[n - 1]) / len(item.average_speed_x[n - 1])

                if mean > next_mean and mean > previous_mean:
                    
                    _ , p_val_low = stats.ttest_ind(item.average_speed_x[n], item.average_speed_x[n - 1])
                    _ , p_val_high = stats.ttest_ind(item.average_speed_x[n], item.average_speed_x[n + 1])
                    if p_val_low < critical_p_val and p_val_high < critical_p_val:
                        print("local maxima (",n,"):", mean, ">", previous_mean, "(p =",p_val_low,");",mean,">",next_mean,"(p =",p_val_high,")")
                        parameters_of_interest.append([item, p_val_low, p_val_high])

                
                #print("not local maxima")

#print(*parameters_of_interest, sep='\n')
#print(*grouped_data, sep='\n')

for item in parameters_of_interest:
    print (item[0].parameters())
    print ("({:2f},{:2f})".format(item[1],item[2]))
    print("")
"""



