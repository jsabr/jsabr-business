
#Basic example showcasing changing a list into a custom object, exporting to 2 different steams
$item_grouping = @("panda","bear")
$obj = @()

foreach($item in $item_grouping){

    $obj += [pscustomobject]@{
        animal=$item
    }
}

Write-Host "Animals in the zoo"

$obj | ForEach-Object { Write-Output $_.animal } 

