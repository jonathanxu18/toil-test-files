cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo
stdout: output.txt
requirements:
  DockerRequirements:
    dockerPull: ubuntu:16.04
inputs:
  message:
    type: string
    inputBinding:
      position: 1
outputs:
  output:
    type: stdout
