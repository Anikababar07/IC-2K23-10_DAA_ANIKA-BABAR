def job_sequencing(jobs):
    # Sort jobs according to profit in decreasing order
    jobs.sort(key=lambda job: job[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Create slots for scheduling jobs
    slots = [False] * max_deadline
    scheduled_jobs = [None] * max_deadline
    total_profit = 0

    # Schedule jobs
    for job_id, deadline, profit in jobs:
        # Find a free slot before or on the deadline
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if not slots[slot]:
                slots[slot] = True
                scheduled_jobs[slot] = job_id
                total_profit += profit
                break

    return scheduled_jobs, total_profit


def main():
    try:
        n = int(input("Enter number of jobs: "))

        if n <= 0:
            print("Please enter a positive number.")
            return

        jobs = []

        print("\nEnter job details:")

        for i in range(n):
            job_id = input(f"\nEnter Job ID for job {i + 1}: ")
            deadline = int(input("Enter deadline: "))
            profit = float(input("Enter profit: "))

            if deadline <= 0:
                print("Deadline must be greater than zero.")
                return

            jobs.append((job_id, deadline, profit))

        scheduled_jobs, total_profit = job_sequencing(jobs)

        print("\nScheduled Jobs:")
        for i, job in enumerate(scheduled_jobs, start=1):
            if job is not None:
                print(f"Slot {i}: {job}")
            else:
                print(f"Slot {i}: Empty")

        print(f"\nMaximum Profit: {total_profit:.2f}")

    except ValueError:
        print("Invalid input! Please enter valid values.")


if __name__ == "__main__":
    main()