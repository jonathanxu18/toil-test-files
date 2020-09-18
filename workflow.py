from toil.common import Toil
from toil.job import Job

def helloWorld(message, memory="3G", cores=2, disk="3G"):
    return f"Hello, world! {message}"

if __name__ == "__main__":
    parser = Job.Runner.getDefaultArgumentParser()
    options = parser.parse_args()
    options.clean = "always"

    root_job = Job.wrapFn(helloWorld, "FIRST JOB")

    for i in range(0, 1000):
        root_job.addChildFn(helloWorld, i)

    with Toil(options) as workflow:
        workflow.start(root_job)
