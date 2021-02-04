import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "monocdk",
    "version": "1.88.0",
    "description": "An experiment to bundle the entire CDK into a single module",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "monocdk",
        "monocdk._jsii",
        "monocdk.alexa_ask",
        "monocdk.app_delivery",
        "monocdk.assets",
        "monocdk.aws_accessanalyzer",
        "monocdk.aws_acmpca",
        "monocdk.aws_amazonmq",
        "monocdk.aws_amplify",
        "monocdk.aws_apigateway",
        "monocdk.aws_apigatewayv2",
        "monocdk.aws_apigatewayv2_integrations",
        "monocdk.aws_appconfig",
        "monocdk.aws_appflow",
        "monocdk.aws_applicationautoscaling",
        "monocdk.aws_applicationinsights",
        "monocdk.aws_appmesh",
        "monocdk.aws_appstream",
        "monocdk.aws_appsync",
        "monocdk.aws_athena",
        "monocdk.aws_auditmanager",
        "monocdk.aws_autoscaling",
        "monocdk.aws_autoscaling_common",
        "monocdk.aws_autoscaling_hooktargets",
        "monocdk.aws_autoscalingplans",
        "monocdk.aws_backup",
        "monocdk.aws_batch",
        "monocdk.aws_budgets",
        "monocdk.aws_cassandra",
        "monocdk.aws_ce",
        "monocdk.aws_certificatemanager",
        "monocdk.aws_chatbot",
        "monocdk.aws_cloud9",
        "monocdk.aws_cloudformation",
        "monocdk.aws_cloudfront",
        "monocdk.aws_cloudfront_origins",
        "monocdk.aws_cloudfront.experimental",
        "monocdk.aws_cloudtrail",
        "monocdk.aws_cloudwatch",
        "monocdk.aws_cloudwatch_actions",
        "monocdk.aws_codeartifact",
        "monocdk.aws_codebuild",
        "monocdk.aws_codecommit",
        "monocdk.aws_codedeploy",
        "monocdk.aws_codeguruprofiler",
        "monocdk.aws_codegurureviewer",
        "monocdk.aws_codepipeline",
        "monocdk.aws_codepipeline_actions",
        "monocdk.aws_codestar",
        "monocdk.aws_codestarconnections",
        "monocdk.aws_codestarnotifications",
        "monocdk.aws_cognito",
        "monocdk.aws_config",
        "monocdk.aws_databrew",
        "monocdk.aws_datapipeline",
        "monocdk.aws_datasync",
        "monocdk.aws_dax",
        "monocdk.aws_detective",
        "monocdk.aws_devopsguru",
        "monocdk.aws_directoryservice",
        "monocdk.aws_dlm",
        "monocdk.aws_dms",
        "monocdk.aws_docdb",
        "monocdk.aws_dynamodb",
        "monocdk.aws_ec2",
        "monocdk.aws_ecr",
        "monocdk.aws_ecr_assets",
        "monocdk.aws_ecs",
        "monocdk.aws_ecs_patterns",
        "monocdk.aws_efs",
        "monocdk.aws_eks",
        "monocdk.aws_eks_legacy",
        "monocdk.aws_elasticache",
        "monocdk.aws_elasticbeanstalk",
        "monocdk.aws_elasticloadbalancing",
        "monocdk.aws_elasticloadbalancingv2",
        "monocdk.aws_elasticloadbalancingv2_actions",
        "monocdk.aws_elasticloadbalancingv2_targets",
        "monocdk.aws_elasticsearch",
        "monocdk.aws_emr",
        "monocdk.aws_emrcontainers",
        "monocdk.aws_events",
        "monocdk.aws_events_targets",
        "monocdk.aws_eventschemas",
        "monocdk.aws_fms",
        "monocdk.aws_fsx",
        "monocdk.aws_gamelift",
        "monocdk.aws_globalaccelerator",
        "monocdk.aws_glue",
        "monocdk.aws_greengrass",
        "monocdk.aws_greengrassv2",
        "monocdk.aws_guardduty",
        "monocdk.aws_iam",
        "monocdk.aws_imagebuilder",
        "monocdk.aws_inspector",
        "monocdk.aws_iot",
        "monocdk.aws_iot1click",
        "monocdk.aws_iotanalytics",
        "monocdk.aws_iotevents",
        "monocdk.aws_iotsitewise",
        "monocdk.aws_iotthingsgraph",
        "monocdk.aws_iotwireless",
        "monocdk.aws_ivs",
        "monocdk.aws_kendra",
        "monocdk.aws_kinesis",
        "monocdk.aws_kinesisanalytics",
        "monocdk.aws_kinesisfirehose",
        "monocdk.aws_kms",
        "monocdk.aws_lakeformation",
        "monocdk.aws_lambda",
        "monocdk.aws_lambda_destinations",
        "monocdk.aws_lambda_event_sources",
        "monocdk.aws_lambda_nodejs",
        "monocdk.aws_lambda_python",
        "monocdk.aws_licensemanager",
        "monocdk.aws_logs",
        "monocdk.aws_logs_destinations",
        "monocdk.aws_macie",
        "monocdk.aws_managedblockchain",
        "monocdk.aws_mediaconnect",
        "monocdk.aws_mediaconvert",
        "monocdk.aws_medialive",
        "monocdk.aws_mediapackage",
        "monocdk.aws_mediastore",
        "monocdk.aws_msk",
        "monocdk.aws_mwaa",
        "monocdk.aws_neptune",
        "monocdk.aws_networkfirewall",
        "monocdk.aws_networkmanager",
        "monocdk.aws_opsworks",
        "monocdk.aws_opsworkscm",
        "monocdk.aws_pinpoint",
        "monocdk.aws_pinpointemail",
        "monocdk.aws_qldb",
        "monocdk.aws_quicksight",
        "monocdk.aws_ram",
        "monocdk.aws_rds",
        "monocdk.aws_redshift",
        "monocdk.aws_resourcegroups",
        "monocdk.aws_robomaker",
        "monocdk.aws_route53",
        "monocdk.aws_route53_patterns",
        "monocdk.aws_route53_targets",
        "monocdk.aws_route53resolver",
        "monocdk.aws_s3",
        "monocdk.aws_s3_assets",
        "monocdk.aws_s3_deployment",
        "monocdk.aws_s3_notifications",
        "monocdk.aws_sagemaker",
        "monocdk.aws_sam",
        "monocdk.aws_sdb",
        "monocdk.aws_secretsmanager",
        "monocdk.aws_securityhub",
        "monocdk.aws_servicecatalog",
        "monocdk.aws_servicecatalogappregistry",
        "monocdk.aws_servicediscovery",
        "monocdk.aws_ses",
        "monocdk.aws_ses_actions",
        "monocdk.aws_signer",
        "monocdk.aws_sns",
        "monocdk.aws_sns_subscriptions",
        "monocdk.aws_sqs",
        "monocdk.aws_ssm",
        "monocdk.aws_sso",
        "monocdk.aws_stepfunctions",
        "monocdk.aws_stepfunctions_tasks",
        "monocdk.aws_synthetics",
        "monocdk.aws_timestream",
        "monocdk.aws_transfer",
        "monocdk.aws_waf",
        "monocdk.aws_wafregional",
        "monocdk.aws_wafv2",
        "monocdk.aws_workspaces",
        "monocdk.cloud_assembly_schema",
        "monocdk.cloudformation_include",
        "monocdk.custom_resources",
        "monocdk.cx_api",
        "monocdk.lambda_layer_awscli",
        "monocdk.lambda_layer_kubectl",
        "monocdk.pipelines",
        "monocdk.region_info"
    ],
    "package_data": {
        "monocdk._jsii": [
            "monocdk@1.88.0.jsii.tgz"
        ],
        "monocdk": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "constructs>=3.2.0, <4.0.0",
        "jsii>=1.15.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ]
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
