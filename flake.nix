{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs }: let
    supportedSystems = [ "x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ];
    forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
    pkgs = forAllSystems (system: nixpkgs.legacyPackages.${system});
  in {
    devShells = forAllSystems (system: {
      default =  pkgs.${system}.mkShell {

        packages = with pkgs.${system}.python312Packages; [
          python
          pkgs.${system}.pyright
          # this should largely reflect `Requirements.txt`
          datetime
          pygame
          pyttsx3
        ];
      };
    });
  };
}
