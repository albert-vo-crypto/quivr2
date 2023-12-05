import Image from "next/image";
import Link from "next/link";

export const Logo = (): JSX.Element => {
  return (
    <Link href={"/"} className="flex items-center gap-4">
      <Image
        className="rounded-full"
        src={"/logo.png"}
        alt="ChatETH Logo"
        width={96}
        height={96}
      />
      <h1 className="font-bold">ChatETH</h1>
    </Link>
  );
};
