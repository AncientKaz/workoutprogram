import datetime
import requests

#--- Keys ---#
PUSHOVER_KEY = "um3e9ioxybhsekhzdjrh1c9hb12et7" # User specific info
PUSHOVER_TOKEN = "axgf7pwvytpq5rseo92bo1pgi36vvp" # For the app

#--- Workout Plan by Day, Separated ---#
GYMWORKOUTS = {
    "Monday Session": {
        "title": "Upper (Chest, Triceps, Shoulders)",
        "exercises":
        [
            "Rowers x30",
            "Pushups x40",
            "30 Minute Cardio Session (60/120s)",
            "Smith Machine Bench Press (4 x 6), inc weight",
            "Supine Bench Press (3 x 6), const weight",
            "Shoulder Press/Skull Crushers (3 x 8), medium weight",
            "Incline Bench Press (DB or Smith) (3 x 10,8,6), inc by 2.5",
            "Cable/Pec Fly (3 x 15), controlled",
            "OH Face Pulls (4 x 12), controlled",
            "Tricep Extensions (4 x 10)"
        ]
    },
    "Tuesday Session": {
        "title": "Back + Biceps",
        "exercises": 
        [
            "Rowers x30",
            "Pushups x40",
            "30 Minute Cardio Sessions (Five Mins On, Five Mins Off)",
            "Lat Pulldowns (4 x 15), 60%, 1 set warmup",
            "Dumbbell Pullovers (2 x 15), controlled",
            "DB Rows (3 x 12), controlled (same weight as DBP)",
            "Preacher Curls (3 x 20), controlled",
            "Hammer Curls (4 x 12), 50%",
            "Seated Rows (4 x 12), 40%"
        ]
    },
    "Wednesday Session": {
        "title": "Legs (Quad Focus)",
        "exercises":
        [
            "High Knees 4 x 10",
            "Motivator 5 downward",
            "Squats (Smith Machine) 5 x 6, 80%",
            "Rear Lunges 4 x 10, last 2 sets 40% weights",
            "Leg Press 2 x 20, 70%",
            "Leg Extensions 4 x 12, 70%",
            "Leg Adductors 2 x 30, 60%",
            "Recovery: Bent Leg Body Twist, Thigh Stretch"
        ]
    }
}
def send_pushover_notification(title, message):
    """Sends a notification to your device via Pushover."""
    if PUSHOVER_KEY == "YOUR_USER_KEY" or PUSHOVER_TOKEN == "YOUR_API_TOKEN":
        print("ERROR: Please replace 'USER_KEY' and 'API_TOKEN' in the script.")
        return
    try:
        response = requests.post("https://api.pushover.net/1/messages.json", data={
            "token": PUSHOVER_TOKEN,
            "user": PUSHOVER_KEY,
            "title": title,
            "message": message,
            "priority": 0 # Normal priority
        })
        response.raise_for_status() # Raise an exception for bad status codes
        print("Notification sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending notification: {e}")
def main():
    # Get date as string and get current day workout
    day_workout=datetime.datetime.now().strftime("%A")
    workout_info = GYMWORKOUTS.get(day_workout)
    notif_title = f"Let's get this workout in broski. Time to grind."
    if workout_info:
        workout_info = workout_info["title"]
        exercises = workout_info["exercises"]
        
        # Build the message string with a title and a bulleted list of exercises
        message_lines = [workout_info]
        for exercise in exercises:
            message_lines.append(f"• {exercise}")
        
        workout_plan = "\n".join(message_lines)
    else:
        # Fallback message if today is not in the WORKOUTS dictionary
        workout_plan = "No workout scheduled for today."
        notification_title = "Rest Day"

    # Send the notification
    send_pushover_notification(notification_title, workout_plan)

if __name__ == "__main__":
    main()