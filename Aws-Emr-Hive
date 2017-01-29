# AWS
AWS Poc's and tests for various  scenerio


aws emr create-cluster \
--applications Name=Hive \
--ec2-attributes '{"KeyName":"Aws-Emr-check","InstanceProfile":"EMR_EC2_DefaultRole","EmrManagedSlaveSecurityGroup":"sg-46895421","EmrManagedMasterSecurityGroup":"sg-47895420"}' \
--service-role EMR_DefaultRole --release-label emr-5.0.0 --name 'emr-hive-execution' \
--instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"m3.xlarge","Name":"MASTER"},{"InstanceCount":2,"InstanceGroupType":"CORE","InstanceType":"m3.xlarge","Name":"CORE"}]' \
--scale-down-behavior TERMINATE_AT_TASK_COMPLETION --region ap-southeast-2

aws emr list-clusters

aws emr list-instances --cluster-id j-9J7T8485CQ0


aws emr describe-cluster --cluster-id j-9J7T8485CQ0



ssh -i Aws-Emr-check.pem hadoop@ec2-13-55-101-119.ap-southeast-2.compute.amazonaws.com


ssh hadoop@ec2-13-54-56-66.ap-southeast-2.compute.amazonaws.com -i Aws-Emr-check.pem


ssh -i Aws-Emr-check.pem hadoop@ec2-13-54-56-66.ap-southeast-2.compute.amazonaws.com


In the security group and the inbound  conections add teh ip address from where to execute else connection time out .


hive

create external table employees (
  name varchar(100),
  gender varchar(10)
)
row format delimited
fields terminated by ','
lines terminated by '\n'
location 's3://employee-upload/';


