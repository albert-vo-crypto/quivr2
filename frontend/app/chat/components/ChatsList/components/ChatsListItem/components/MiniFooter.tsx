import { DISCORD_URL, GITHUB_URL, TWITTER_URL } from "@/lib/config/CONSTANTS";

export const MiniFooter = (): JSX.Element => {
  return (
    <footer className="bg-white dark:bg-black border-t dark:border-white/10 mt-auto py-4">
      <div className="max-w-screen-xl mx-auto flex justify-center items-center gap-4">
        Built using Quivr, Supabase, ChatGPT, Jupyter Notebook
        <a
          href={GITHUB_URL}
          target="_blank"
          rel="noopener noreferrer"
          aria-label="Quivr GitHub"
        >
          <img
            className="h-4 w-auto dark:invert"
            src="/github2.svg"
            alt="GitHub"
          />
        </a>
        <a
          href={TWITTER_URL}
          target="_blank"
          rel="noopener noreferrer"
          aria-label="Quivr Twitter"
        >
          <img className="h-4 w-auto" src="/twitter2.svg" alt="ALT2" />
        </a>

        <a
          href={DISCORD_URL}
          target="_blank"
          rel="noopener noreferrer"
          aria-label="Quivr Discord"
        >
          <img className="h-4 w-auto" src="/discord2.svg" alt="ALT3" />
        </a>
   

      </div>
    </footer>
  );
};
