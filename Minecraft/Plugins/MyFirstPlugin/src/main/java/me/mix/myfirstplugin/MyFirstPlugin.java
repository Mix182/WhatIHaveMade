package me.mix.myfirstplugin;

import org.bukkit.plugin.java.JavaPlugin;

public final class MyFirstPlugin extends JavaPlugin {

    @Override
    public void onEnable() {
        // Plugin startup logic

        System.out.println("Mi first plugin has started!!! :D");

        getCommand("gui").setExecutor(new GUICommand());
        getServer().getPluginManager().registerEvents(new MenuHandeler(), this);
    }
    @Override
    public void onDisable() {
        // Plugin shutdown logic
        System.out.println("MyFirstPlugin Shut down sucssesfully!!!");
    }
}
