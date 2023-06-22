function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((error) => {
        if (error) {
          console.error('Job creation failed:', error);
          return;
        }
        console.log('Notification job created:', job.id);
      });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (error) => {
      console.error(`Notification job ${job.id} failed:`, error);
    });

    job.on('progress', (progress, expectedTotal) => {
      const percentage = Math.round((progress / expectedTotal) * 100);
      console.log(`Notification job ${job.id} ${percentage}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
