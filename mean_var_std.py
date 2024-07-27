import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')        

    else:
        #print(list)
        arr_list = np.array(list).reshape(3,3)
        #print(arr_list)

        mean_rows = arr_list.mean(axis=0)
        mean_columns = arr_list.mean(axis=1)
        mean_flatten = arr_list.mean()
        variance_rows = arr_list.var(axis=0)
        variance_columns = arr_list.var(axis=1)
        variance_flatten = arr_list.var()
        std_rows = arr_list.std(axis=0)
        std_columns = arr_list.std(axis=1)
        std_flatten = arr_list.std()
        max_rows = arr_list.max(axis=0)
        max_columns = arr_list.max(axis=1)
        max_flatten = arr_list.max()
        min_rows = arr_list.min(axis=0)
        min_columns = arr_list.min(axis=1)
        min_flatten = arr_list.min()
        sum_rows = arr_list.sum(axis=0)
        sum_columns = arr_list.sum(axis=1)
        sum_flatten = arr_list.sum()

        calculations = {}

        calculations['mean'] = [mean_rows.tolist(),mean_columns.tolist(),mean_flatten.tolist()]
        calculations['variance'] = [variance_rows.tolist(),variance_columns.tolist(),variance_flatten.tolist()]
        calculations['standard deviation'] = [std_rows.tolist(),std_columns.tolist(),std_flatten.tolist()]
        calculations['max'] = [max_rows.tolist(),max_columns.tolist(),max_flatten.tolist()]
        calculations['min'] = [min_rows.tolist(),min_columns.tolist(),min_flatten.tolist()]
        calculations['sum'] = [sum_rows.tolist(),sum_columns.tolist(),sum_flatten.tolist()]
    return calculations
