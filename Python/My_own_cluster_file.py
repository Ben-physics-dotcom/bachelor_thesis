class My_own_cluster_file():
  def dimension_reduction(tc_matrix,st):
    n = len(tc_matrix)
    tc_value = []
    column = [] # choosen constant crytall, index
    row = [] # choosen variable crystall,index
    col_crystall = []
    row_crystall = []
    time_to_find = []
    for i in range(n):
      for j in range(n):
        start = time()
        ind = df_tc.columns[i]
        a = df_tc[ind][j]
        if a >= st and int(round(a,4))!=1:
          tc_value.append(a)
          column.append(i)
          row.append(j)
          col_crystall.append(ind)
          row_crystall.append(df_tc.index[j])
          end = time()
          t = round(end-start,7)
          time_to_find.append(t)
          # print(f'Index: col={i} row={j}, Time: {t}s, a={a}')
    df = pd.DataFrame(
      {
          'Tc Value':tc_value,
          'Column':column,
          'Row':row,
          'Column Crystal':col_crystall,
          'Row Crystall':row_crystall,
          'Time to Find [s]':time_to_find
      }
    )
    return df


  # Function to get orphans from a specified column
  def cluster(df, column,count=1):
      # Count the occurrences of each element in the column
      counts = df[column].value_counts()
      # Filter the elements that appear only once
      orphans = counts[counts == count].index
      # Create a new DataFrame with orphans
      orphan_df = df[df[column].isin(orphans)]
      return orphan_df
  def drop_orphans(df,column):
    counts = df[column].value_counts()
    t = counts[counts == 1].index
    orphan_indices = df[df[column].isin(t)].index
    # Drop rows with orphan elements from the DataFrame
    df = df.drop(orphan_indices)
    return df

  def cl_hist(df, column):
    # Get the counts of each unique value in the column
    counts = df[column].value_counts()

    # Create a dictionary to map each unique value to its cluster number
    cluster_dict = {value: count for value, count in counts.items()}

    # Map the original column to the cluster numbers using the dictionary
    df['cl numb'] = df[column].map(cluster_dict)

    return df
