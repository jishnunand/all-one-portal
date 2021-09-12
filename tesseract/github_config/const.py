APP_NAME_YAML = {
    "config": {
        "pipelineSettings": {
            "jenkinsNode": "Linux_Agent_2",
            "stages": [
                {
                    "Build": {
                        "script": "buildMaven"
                    }
                },
                {
                    "SonarQubeAnalysis": {
                        "script": "sonarScan"
                    }
                },
                {
                    "veracode": {
                        "script": "veracodescan"
                    }
                },
                {
                    "DeployArtifactory": {
                        "script": "storeArtifactWms"
                    }
                }
            ],
            "genericSettings": {
                "deliverableFileType": "jar"
            }
        },
        "notifySettins": {
            "notify": "jishnunand@gmail.com",
            "notifyWhen": "ANY"
        }
    }
}
