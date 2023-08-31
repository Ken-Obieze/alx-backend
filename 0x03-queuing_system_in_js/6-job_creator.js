import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message.',
};

const job = queue.create('push_notification_code', jobData);

job
  .on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  })
  .on('complete', () => {
    console.log('Notification job completed');
    queue.shutdown(0);
  })
  .on('failed', () => {
    console.log('Notification job failed');
    queue.shutdown(1);
  });

job.save();
