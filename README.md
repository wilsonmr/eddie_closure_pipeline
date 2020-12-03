# Template for running fits on Eddie

Here is a template for running multiple fits on eddie, with as much automation
as possible.

In the `templates` directory you will find the job submission script templates
and base fit runcard which should be edited by the user depending on resources
required, email notification settings etc. The template should be fairly self
explanatory and there are further instructions on the [wiki](https://www.wiki.ed.ac.uk/display/ResearchServices/Eddie)

The next step is to update the `user_settings.ini` file to change the base name
i.e for `191015-mw-001` its the `191015-mw-` part. I also recommend making the
description for the fit have a trailing space so the 3 digit number gets
appended nicely. Here you can also specify the target number of replicas as
well as the number of replicas to run for each fit. I would recommend specifying
things here rather than hardcoding them in the templates as much as possible.

The next step is to check the submit_fits script. The basic usage is:

```bash
$ ./submit_fits 1 10
```

which would run fits `001` to `010`. If you just want to run a single fit you
can either edit this script or just specify the start and end fit as the same
number.

```bash
$ ./submit_fits 1 1
```

The script goes through each fit to be ran, creates the submission scripts and
the fit runcard and then submits the setup job, the fit array job and finally
the post fit job. For n3fit closure test the setup job creates the fake closure
data, the fit job performs the fit and the post fit evolves the replicas and
runs postfit. The fit job waits for the setup job to complete, similarly the
postfit job waits for the replicas to finish. This is achieved using `-hold_jid`
`SGE` option along with the name of the relvant fit. This is why we specify the
name on the commandline, because it's easier to pass it to the next job.

By default an email is sent
once the post fit job has finished, you should then log on and check the relevant
`.log` file to
make sure the post fit succeeded and then upload the fit/s using `upload`.

A lot of the scripts rely on how I've set up my environment, `conda` etc. but
hopefully this will provide a template for doing something similar.
