from toil.common import Toil
from toil.job import Job

def helloWorld(job, message, memory="3G", cores=2, disk="3G"):
    job.log(f"Hello, world! {message}")

if __name__ == "__main__":
    parser = Job.Runner.getDefaultArgumentParser()
    options = parser.parse_args()
    options.clean = "always"

    parent_job = Job.wrapJobFn(helloWorld, "FIRST JOB")

    for i in range(0, 100):
        parent_job.addChildJobFn(helloWorld, i)

    with Toil(options) as workflow:
        workflow.start(parent_job)
