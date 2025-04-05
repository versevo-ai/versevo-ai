export default function JoinWaitlist() {
    return (
      <div>
        <form className="flex w-[600px] h-[45px] rounded-[40px] overflow-hidden shadow-md flex-row bg-transparent">
          <input
            type="email"
            placeholder="Enter your Email Address"
            className="w-full px-6 text-xl text-blue-900 bg-blue-100 focus:outline-none"
            required
          />
          <button
            type="submit"
            className="w-[198px] text-xl text-blue-900 bg-green-300 hover:bg-green-400 transition-colors"
          >
            Join Waitlist
          </button>
        </form>
      </div>
    );
  }
  