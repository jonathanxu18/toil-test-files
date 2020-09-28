cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo
hints:
  DockerRequirement: 
    dockerPull: ubuntu:16.04
stdout: output.txt
inputs:
  - id: message
    type: string
    inputBinding:
      position: 1
outputs:
  - id: output
    type: File
    outputBinding:
      glob: output.txt
