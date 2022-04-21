class FrequencyEcoder:
    
    def __init__(self,data):
        
        self.data=data
    

        
        
   ########### Computer frequency in each row #######     
        
    def frequency_computer(self,string):

        string=string.split()
        
        dict_freq={}
        
        freq_list=[]
        
        for i in string:
            if i not in freq_list:
    #             print(i)
                freq_list.append(i)
        for j in range(0,len(freq_list)):
            dict_freq[freq_list[j]]=string.count(freq_list[j])
        return dict_freq
    
    ###### convert row into dictionary #######
    
    def row_to_dict(self):
        inputs=self.data
        for index, item in inputs.items():
            inputs[index]=remove_char(item).replace('br br',' ')
            for _ in inputs[index]:
                if type(_)==int:
                    inputs[index]=item.replace('_',' ')

            inputs[index]=frequency_computer(inputs[index])
        return inputs
    
    
####### Convert row into the list #######
        
    def conv(self,stock_str):
        n=int(input('Enter the number of rows modify: '))
        for i in range(n):
    #         print(stock_str[i])
            liste=stock_str[i].split()
    #         st=','.join([item  for item in liste])
            stock_str[i]=liste

        return stock_str[:n]
    
    def dict_combine_2(self,dic1,dic2):    
        return dict(sorted({k: dic1.get(k, 0) + dic2.get(k, 0) for k in set(dic1) | set(dic2)}.items()))
    
    ##### ENCODING DOCUMENT ######
    def final_encoder(self):
        dict_store=self.row_to_dict_to_dict()
        
        start=dict_store[0]

        for i in range(1,len(dict_store)):
            var=self.dict_combine_2(start,dict_store[i])
            start=var
        return start
    
    
    
    ####### Transform the csv file###########
    
    def transform(self):
        
        temp = self.conv(new_input)
        
        ff=self.final_encoder(inputs[:5])
        
        final = []
        new_df = temp.copy()
        for idx,item in enumerate(temp):
            final = []
            for x in item:
                if x in ff.keys():
                    final.append(ff[x])
            new_df[idx] = final
        
        return new_df
    