Function Get-PolicySchema {
    Param(
        [Parameter(Mandatory = $false)]
        [String] $schemaURL = "https://schema.management.azure.com/schemas/2018-05-01/policyDefinition.json",

        [Parameter(Mandatory = $false)]
        [String] $schemaFilePath = ".\policySchema.json"
    )

    # Download File
    $res = Invoke-WebRequest -Uri $schemaURL -Method GET

    # Parse for JSON
    $jsonString = $res.RawContent.Substring($res.RawContent.indexOf('{'))

    # Output Schema to file
    $jsonString | Out-File -Force -FilePath $schemaFilePath
}

Function Test-PolicySchema {
    Param(
        [Parameter(Mandatory = $true)]
        [String] $policyJson,

        [Parameter(Mandatory = $true)]
        [String] $policySchema
    )

    # 
}