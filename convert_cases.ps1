param(
    [string]$Root = ".\cases"
)

Get-ChildItem -Path $Root -Recurse -Filter *.docx | ForEach-Object {
    $mdPath = Join-Path $_.Directory "$($_.BaseName).md"

    if (-not (Test-Path $mdPath)) {
        pandoc $_.FullName -t gfm -o $mdPath --wrap=none
        Write-Host "Created $mdPath"
    }
}
