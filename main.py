import pandas as pd

def main():
    apex_class_data = pd.read_csv('apex_classes.csv', usecols=['Id', 'NamespacePrefix', 'Name'])
    async_jobs_data = pd.read_csv('async_apex_jobs.csv', usecols=['Id','ApexClassId', 'CronTriggerId'])
    cron_job_data = pd.read_csv('cron_job_details.csv', usecols=['Id','Name'])
    cron_trigger_data = pd.read_csv('cron_triggers.csv', usecols=['Id','CronJobDetailId', 'CronExpression'])

    df_async = pd.DataFrame(async_jobs_data)
    df_async = df_async.rename(columns={'Id': 'AsyncJobId' })
    df_apex = pd.DataFrame(apex_class_data)
    df_apex = df_apex.rename(columns={'Id': 'ApexClassId', 'Name': 'ApexClassName'})
    df_cron_job = pd.DataFrame(cron_job_data)
    df_cron_job = df_cron_job.rename(columns={'Id': 'CronJobDetailId' })
    df_cron_trigger = pd.DataFrame(cron_trigger_data)

    inner_join = pd.merge(df_async, 
                      df_apex, 
                      left_on ='ApexClassId',
                      right_on ='ApexClassId',
                      how ='inner')
    df_cron_trigger = pd.merge(df_cron_trigger, 
                      df_cron_job, 
                      left_on ='CronJobDetailId',
                      right_on ='CronJobDetailId',
                      how ='inner')

    df_cron_trigger = pd.merge(df_cron_trigger, 
                      inner_join, 
                      left_on ='Id',
                      right_on ='CronTriggerId',
                      how ='inner')
    
    #  df_cron_trigger.to_csv('output.csv')
    with open('output.txt', 'w') as f:
        for index, row in df_cron_trigger.iterrows():
            apexName = row['ApexClassName']
            if pd.notnull(row['NamespacePrefix']):
                apexName = f"{row['NamespacePrefix']}.{apexName}"
            f.write(f"System.schedule('{row['Name']}', '{row['CronExpression']}', new {apexName}());\n")
        

if __name__ == '__main__':
    main()